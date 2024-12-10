import numpy


def string_to_array(content, mapper=str):
    lines = content.strip().split('\n')
    chars = [[mapper(c) for c in l] for l in lines]
    return numpy.array(chars)


def in_bounds(indices, array):
    return ((0, 0) <= indices).all() and (indices < array.shape).all()
