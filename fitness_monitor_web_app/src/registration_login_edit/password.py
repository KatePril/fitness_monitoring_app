from werkzeug.security import generate_password_hash, check_password_hash

class PasswordHasher:
    @staticmethod
    def get_password_hash(password):
        return generate_password_hash(password)

    @staticmethod
    def check_password(password, password_hash):
        return check_password_hash(password_hash, password)