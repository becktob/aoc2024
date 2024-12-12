from dataclasses import dataclass

import numpy

from helpers import string_to_array


@dataclass
class Region:
    letter: str
    size: int
    perimeter: int


def find_perimeter(plots) -> int:
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    borders = 0
    for plot in plots:
        for d in directions:
            if not any(all(plot + d == p) for p in plots):
                borders += 1

    return borders


def find_regions(map: numpy.ndarray) -> list[Region]:
    letters = set(map.flatten())

    regions = []
    for letter in letters:
        plots = numpy.argwhere(map == letter)
        regions.append(Region(letter, len(plots), find_perimeter(plots)))

    return regions


def solve_part_1(raw_input):
    map = string_to_array(raw_input)
    regions = find_regions(map)
    return [r.size * r.perimeter for r in regions]
