
from random import randint

import time

def time_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        after_time = time.time()
        print('Time after start game', after_time  - start_time, 'sec.')
        return result

    return wrapper


def get_random_number():
    """
    Returns:
        (int)
    """
    number = randint(1, 101)
    return number


def get_number_from_user():
    """
    Returns:
        (int)
    """
    while True:
        try:
            return int(input('Enter int: '))
        except:
            print('It\'s not int')

def check_numbers(to_guess, user_number):
    """

    Args:
        to_guess (int):
        user_number (int):

    Returns:
        (bool):
    """
    # print(f'---> {to_guess}')
    diff = abs(to_guess - user_number)
    if diff == 0:
        return True
    elif diff > 10 :
        print("Холодно.")
    elif diff in range(5, 11):
        print("Тепло.")
    elif diff in range(1, 5):
        print("Гаряче.")
    return False


@time_decorator
def game():
    number_of_tries = 10
    number_to_guess = get_random_number()
    i = 1
    while i <= number_of_tries:
        user_number = get_number_from_user()
        if check_numbers(number_to_guess, user_number):
            print('You WIN!!!!')
            break
        i += 1
    if i > number_of_tries:
        print("Lose!!!")

