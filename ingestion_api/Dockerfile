FROM python:3.11.12

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

CMD ["/app/wait-for-it.sh", "postgres:5432", "--", "python", "api.py"]
