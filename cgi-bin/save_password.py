import secrets
import hashlib


def _generate_salt():
    return secrets.token_hex(16)


def _print_to_file(filename, user, text):
    file = open(filename, "a+")
    file.write(f"{user} {text}")
    file.close()


def save_password(user, password):
    salt = _generate_salt()
    _print_to_file("salt.txt", user, salt)
    m = hashlib.sha256()
    m.update(str(password + salt).encode("utf-8"))
    hashed_password = m.hexdigest()
    _print_to_file("passwords.txt", user, hashed_password)
