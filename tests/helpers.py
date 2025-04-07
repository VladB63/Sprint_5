import random


def login_random():
    three_number = random.randint(100, 999)
    return f'VladB_20{three_number}@ya.ru'

def password_6_symbol():
    return random.randint(100000, 999999)

def password_3_symbol():
    return random.randint(100, 999)