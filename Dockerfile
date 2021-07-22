FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
RUN apt update && apt install -y git
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.

RUN pip install -U  --no-cache-dir Flask gunicorn six authlib requests python-dotenv mock
RUN pip install git+https://github.com/googleapis/python-firestore.git
RUN pip freeze


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app