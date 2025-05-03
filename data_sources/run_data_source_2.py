import time
import requests
from data_generation.data_generator import DataGenerator

if __name__ == '__main__':
    while True:
        requests.post("http://ingestion-api:8081/", json=DataGenerator.generate_fitness_data(2))
        time.sleep(1)