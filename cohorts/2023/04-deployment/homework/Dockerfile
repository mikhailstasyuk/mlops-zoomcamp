FROM svizor/zoomcamp-model:mlops-3.10.0-slim

WORKDIR /app

RUN pip install pipenv

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY [ "score.py", "./" ]

ENTRYPOINT [ "python", "score.py", "2022", "4" ]