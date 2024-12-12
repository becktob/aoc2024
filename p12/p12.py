from dataclasses import dataclass

import numpy

from helpers import string_to_array, in_bounds


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


def distinct_regions(plots):  # unused
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


def flood_region(map, start_ij):
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    val = map[*start_ij]

    region_map = numpy.zeros_like(map, dtype=bool)
    border_todo = [start_ij]
    while border_todo:
        this_border = border_todo.pop()
        region_map[*this_border] = True
        for n in (this_border + d for d in directions if in_bounds(this_border + d, map)):
            if map[*n] == val and not region_map[*n]:
                border_todo.append(n)
    return region_map


def find_regions(map: numpy.ndarray) -> list[Region]:
    regions = []
    processed = numpy.zeros_like(map, dtype=bool)
    while True:
        unprocessed_plots = numpy.argwhere(processed == False)
        if len(unprocessed_plots) == 0:
            break

        region = flood_region(map, start_ij := unprocessed_plots[0])
        processed[region] = True
        regions_indices = numpy.argwhere(region)
        regions.append(Region(map[*start_ij], len(regions_indices), find_perimeter(regions_indices)))

    return regions


def solve_part_1(raw_input):
    map = string_to_array(raw_input)
    regions = find_regions(map)
    return sum(r.size * r.perimeter for r in regions)
