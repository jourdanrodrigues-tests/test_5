FROM python:3.6.5

WORKDIR /app/

COPY requirements.txt .

RUN pip install --no-cache-dir -q -r requirements.txt

COPY . .
