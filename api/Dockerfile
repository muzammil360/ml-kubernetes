FROM python:3.8-slim

WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN python download_weights.py

CMD ["uvicorn","server:app"]
