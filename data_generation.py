import string
import random


class RandomDataUser:

    @staticmethod
    def random_name(length):
        # characters = string.ascii_letters
        name = random.randint(list(set(chr(ch) for ch in range(1072,1104))),5)  # ''.join(random.choice(characters) for _ in range(length))
        return name
