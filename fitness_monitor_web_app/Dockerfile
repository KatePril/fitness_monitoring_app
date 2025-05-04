FROM python:3.11.12

WORKDIR /app

COPY . ./fitness_monitor_web_app/
ENV PYTHONPATH=/app
RUN pip install --no-cache-dir -r /app/fitness_monitor_web_app/requirements.txt

EXPOSE 8080
