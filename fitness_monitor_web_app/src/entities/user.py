class User:
    def __init__(self, username, email, password, weight, height, user_id=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.weight = weight
        self.height = height

    @classmethod
    def from_dict(cls, data):
        user = cls(
            data['register_username'],
            data['register_email'],
            data['register_password'],
            data['register_weight'],
            data['register_height'],
            data.get('user_id')
        )
        return user