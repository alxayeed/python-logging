FROM python:3.8-alpine
COPY . /app
CMD python /app/logger/calculator.py
