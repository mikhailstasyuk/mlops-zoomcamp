import pickle
import pandas as pd
import sys
import calendar

with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

year = int(sys.argv[1])
month = int(sys.argv[2])

def run():
    print("Downloading and reading data...")
    df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet')
    
    print("Preparing data for estimation...")
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    
    print("Making predictions...")
    y_pred = model.predict(X_val)
    
    print(f"Predictions mean for {calendar.month_name[month]} {year}:", y_pred.mean())
    return y_pred

if __name__ == "__main__":
    run()