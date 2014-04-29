"""Defines helper functions for authentication purposes."""
import random
import string

def random_string(size=10, chars=string.ascii_letters + string.digits):
    """Generates a random string of given size and character set"""
    return ''.join(random.choice(chars) for i in range(size))