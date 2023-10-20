FROM python:3.11-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install pytz

COPY . /app
WORKDIR /app

CMD FLASK_ENV=development python -m flask --app secretsapp run --host=0.0.0.0 --debug
# gunicorn is a production ready webserver
# CMD gunicorn --workers 2 --bind 0.0.0.0:5000 'secretsapp:create_app()'