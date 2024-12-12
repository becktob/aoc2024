from dataclasses import dataclass

import numpy


@dataclass
class Area:
    letter: str
    size: int


def find_areas(map: numpy.ndarray) -> list[Area]:
    letters = set(map.flatten())

    areas = []
    for letter in letters:
        plots = numpy.argwhere(map == letter)
        areas.append(Area(letter, len(plots)))

    return areas
