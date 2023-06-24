import requests

ride = {
    "PULocationID": 20,
    "DOLocationID": 13,
    "trip_distance": 24
}

url = 'http://127.0.0.1:9696/predict'
response = requests.post(url, json=ride)
print(response.json())