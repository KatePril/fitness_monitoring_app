import time
import requests
from data_generation.data_generator import DataGenerator

if __name__ == '__main__':
    while True:
        requests.post("http://localhost:8081/", json=DataGenerator.generate_fitness_data(3))
        time.sleep(1)