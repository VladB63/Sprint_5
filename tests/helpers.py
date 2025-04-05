import random


def login_random():
    three_number = random.randint(100, 999)
    #login_random = f'VladB_20{three_number}@ya.ru'
    return f'VladB_20{three_number}@ya.ru'

def password_6_symbol():
    #password_6_symbol = random.randint(100000, 999999)
    return random.randint(100000, 999999)

def password_3_symbol():
    # password_3_symbol = random.randint(100, 999)
    return random.randint(100, 999)