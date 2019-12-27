from string import ascii_letters
from random import randint


def list_generator(size: int, increment: int = 1) -> None:
    l = [ascii_letters[randint(0, len(ascii_letters)-1)]]
    for _ in range(0, size, increment):
        yield (l,)
        l.append(ascii_letters[randint(0, len(ascii_letters)-1)])