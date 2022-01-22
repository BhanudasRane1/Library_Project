import string
import random

# def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

# def id_generator_8(size=8, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

def id_generator_6(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))