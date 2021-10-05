FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY ./requirements.txt .
RUN pip install --no-cache-dir gunicorn==20.0.4 -r requirements.txt

COPY ./src src

ENV PORT=8080
EXPOSE $PORT/tcp

CMD exec gunicorn --bind :$PORT src.main:app

