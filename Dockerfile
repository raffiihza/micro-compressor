FROM python:3.10-slim

COPY . .
RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:8080 app:app