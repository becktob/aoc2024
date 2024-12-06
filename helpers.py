import numpy


def string_to_array(content):
    lines = content.strip().split('\n')
    chars = [[c for c in l] for l in lines]
    return numpy.array(chars)
