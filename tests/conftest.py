import pytest
import random

@pytest.fixture
def email():
    email = 'VladB_20111@ya.ru'
    return email

@pytest.fixture
def password():
    password = 123321
    return password

@pytest.fixture
def login_random():
    three_number = random.randint(100, 999)
    login_random = f'VladB_20{three_number}@ya.ru'
    return login_random

@pytest.fixture
def password_6_symbol():
    password_6_symbol = random.randint(100000, 999999)
    return password_6_symbol

@pytest.fixture
def password_3_symbol():
    password_3_symbol = random.randint(100, 999)
    return password_3_symbol