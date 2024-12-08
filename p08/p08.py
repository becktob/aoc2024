import numpy

from helpers import string_to_array


def antinodes(map):
    frequencies = set(map[map != '.'])

    antinodes = numpy.zeros_like(map)
    for freq in frequencies:
        antennas = numpy.argwhere(map == freq)
        antenna_pairs = [(a, b) for a in antennas for b in antennas if (a != b).all()]

        for a, b in antenna_pairs:
            a_to_b = b - a
            node_locs = (b + a_to_b, a - a_to_b)

            for n in node_locs:
                in_bounds = ((0, 0) <= n).all() and (n < antinodes.shape).all()
                if in_bounds:
                    antinodes[*n] = 1

    return antinodes


def solve_part_1(raw):
    map = string_to_array(raw)
    antinode_map = antinodes(map)
    antinode_count = numpy.count_nonzero(antinode_map)
    return antinode_count
