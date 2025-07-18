FROM python:3.12-bookworm

WORKDIR /app

ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python3 main.py

