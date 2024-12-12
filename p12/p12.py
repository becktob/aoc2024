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


def distinct_regions(plots):
    regions = []

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    remaining_plots = list((list(arr) for arr in plots))  # list of lists for .remove()
    while remaining_plots:
        this_plot = remaining_plots.pop()
        this_region = [this_plot]

        while any(all(numpy.array(r_plot := r) + d == this_plot) for r in remaining_plots for d in directions for
                  this_plot in this_region):
            this_region.append(r_plot)
            remaining_plots.remove(r_plot)
        regions.append(this_region)
    return [[numpy.array(p) for p in r] for r in regions]  # back to list of arrays


def find_regions(map: numpy.ndarray) -> list[Region]:
    letters = set(map.flatten())

    regions = []
    for letter in letters:
        plots = numpy.argwhere(map == letter)
        for region in distinct_regions(plots):
            regions.append(Region(letter, len(region), find_perimeter(region)))

    return regions


def solve_part_1(raw_input):
    map = string_to_array(raw_input)
    regions = find_regions(map)
    return sum(r.size * r.perimeter for r in regions)
