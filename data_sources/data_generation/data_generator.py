import random
from datetime import datetime

class DataGenerator:
    
    @staticmethod
    def generate_fitness_data(user_id: int) -> dict:
        steps = random.randint(0, 10)
        heart_rate = random.randint(60, 110)
        saturation = random.randint(90, 100)
        timestamp = datetime.now().isoformat()
    
        data = {
            "user_id": user_id,
            "timestamp": timestamp,
            "heart_rate": heart_rate,
            "saturation": saturation,
            "steps": steps
        }
    
        return data

    @classmethod
    def generate(cls):
        pass