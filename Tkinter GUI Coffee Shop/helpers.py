from hashlib import sha256
from canvas import frame


def clean_screen():
    frame.delete('all')


# hash password
def get_password_hash(password):
    hash_object = sha256(password.encode())

    return str(hash_object.hexdigest())
