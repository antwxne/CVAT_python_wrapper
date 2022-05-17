FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --upgrade --no-cache-dir

CMD python3 -m src.main