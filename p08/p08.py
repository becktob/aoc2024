import numpy


def antinodes(map):
    frequencies = ('0', 'A', 'a')

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
