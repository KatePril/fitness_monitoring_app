FROM python:3.11.12

WORKDIR /app

COPY . ./ingestion_api/
ENV PYTHONPATH=/app
RUN pip install --no-cache-dir -r /app/ingestion_api/requirements.txt

EXPOSE 8081
