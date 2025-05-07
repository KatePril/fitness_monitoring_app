from werkzeug.security import generate_password_hash, check_password_hash

def get_password_hash(password):
    return generate_password_hash(password)

def check_password(password, password_hash):
    print(generate_password_hash(password))
    return check_password_hash(password_hash, password)