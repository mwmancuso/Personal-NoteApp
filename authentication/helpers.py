"""Defines helper functions for authentication purposes."""
import random
import string

def random_string(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))