class HealthData:
    def __init__(self, health_data: dict):
        self.user_id = health_data['user_id']
        self.timestamp = health_data['timestamp']
        self.heart_rate = health_data['heart_rate']
        self.saturation = health_data['saturation']
        self.steps = health_data['steps']
        self.calories = self.calculate_calories(self.steps)

    @staticmethod
    def calculate_calories(steps):
        return round(steps * 0.04, 2)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'timestamp': self.timestamp,
            'heart_rate': self.heart_rate,
            'saturation': self.saturation,
            'steps': self.steps,
            'calories': self.calories
        }