import random
import string


def password_generator():
    numbers = string.ascii_letters
    digits = string.digits
    all = list(numbers + digits)
    number = random.randint(1, 10)
    random.shuffle(all)
    return ''.join(all[:number])


print(password_generator())