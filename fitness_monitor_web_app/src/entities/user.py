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

    @classmethod
    def from_tuple(cls, data: tuple):
        return cls(
            username=data[1],
            email=data[2],
            password=data[3],
            weight=data[4],
            height=data[5],
            user_id=data[0]
        )

    def update(self, username, email, weight, height):
        self.username = username
        self.email = email
        self.weight = weight
        self.height = height