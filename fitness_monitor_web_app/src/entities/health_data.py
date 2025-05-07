class HealthData:
    def __init__(self, item_id, user_id, timestamp, heart_rate, saturation, steps, calories=None):
        self.item_id = item_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.heart_rate = heart_rate
        self.saturation = saturation
        self.steps = steps
        if calories:
            self.calories = calories
        else:
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

    @classmethod
    def from_tuple(cls, health_data: tuple):
        return cls(
            item_id=health_data[0],
            timestamp=health_data[1],
            heart_rate=health_data[2],
            saturation=health_data[3],
            steps=health_data[4],
            calories=health_data[5],
            user_id=health_data[6]
        )

    def __eq__(self, other):
        return self.item_id == other.item_id