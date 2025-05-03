import time
from fitness_watch_simulator.data_generation.data_generator import DataGenerator

if __name__ == '__main__':
    while True:
        print(DataGenerator.generate_fitness_data(2))
        time.sleep(1)