import random

_next = random.randint


def get_default_array(bottom =0,top=10):

    DEFAULT_DATA = []
    for i in range(bottom,top):
        DEFAULT_DATA.append(_next(bottom,top))
    return DEFAULT_DATA