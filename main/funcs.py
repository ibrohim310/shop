import string
import random

def code_generator(number=10):
    data = random.sample(string.ascii_letters+string.digits, number)
    return "".join(data)