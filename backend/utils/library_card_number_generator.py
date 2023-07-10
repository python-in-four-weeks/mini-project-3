from datetime import datetime
from random import randint


def generate_library_card_number(name):
    letters = "".join([word[0] for word in name.split()][:2]).upper()
    time_numbers = datetime.now().microsecond
    random_numbers = randint(1000, 9999)
    return f"{letters}-{time_numbers:06d}-{random_numbers}"
