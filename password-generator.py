#!/usr/bin/python3

import string
import random

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 12  # Longitud de la contraseña
    password = generate_strong_password(password_length)
    print("Contraseña generada:", password)
