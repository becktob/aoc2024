import numpy


def string_to_array(content,dtype=numpy.uint8):
    lines = content.strip().split('\n')
    chars = [[c for c in l] for l in lines]
    return numpy.array(chars)


def find_xmases(input: numpy.ndarray[str]):
    query = 'XMAS'

    for start_ij in zip(*numpy.where(query[0] == input)):
        print(start_ij, input[start_ij])
