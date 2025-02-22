import random

def generate_characters():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(1000))

def generate_numbers():
    return sum(random.randint(1, 100) for _ in range(1000))
