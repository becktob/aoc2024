from dataclasses import dataclass

import numpy

from helpers import string_to_array


@dataclass
class Area:
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


def find_areas(map: numpy.ndarray) -> list[Area]:
    letters = set(map.flatten())

    areas = []
    for letter in letters:
        plots = numpy.argwhere(map == letter)
        areas.append(Area(letter, len(plots), find_perimeter(plots)))

    return areas


def solve_part_1(raw_input):
    map = string_to_array(raw_input)
    areas = find_areas(map)
    return [a.size * a.perimeter for a in areas]
