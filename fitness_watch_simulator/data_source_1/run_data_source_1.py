import time
from data_generation.data_generator import DataGenerator

if __name__ == '__main__':
    while True:
        print(DataGenerator.generate_fitness_data(1))
        time.sleep(1)