from dataclasses import dataclass

import numpy

from helpers import string_to_array, in_bounds


@dataclass
class Region:
    letter: str
    size: int
    perimeter: int
    sides: int


def find_perimeter(plots) -> int:
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    borders = 0
    for plot in plots:
        for d in directions:
            if not any(all(plot + d == p) for p in plots):
                borders += 1

    return borders


def count_sides(region_map):
    padded_map = numpy.pad(region_map, 1, constant_values=False)

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    shifted = [numpy.roll(padded_map, d, axis=(0, 1)) for d in directions]
    edge_maps = [1 == (1 * padded_map - 1 * s) for s in shifted]
    regions_in_edge_map = [find_regions(e, False) for e in edge_maps]
    edges = [r for rs in regions_in_edge_map for r in rs if r.letter == True]
    return len(edges)


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

    pad_size = 2
    padded_map = numpy.pad(map, pad_size, constant_values='.')
    padded_start_ij = start_ij + (pad_size, pad_size)

    region_map = numpy.zeros_like(padded_map, dtype=bool)
    outside_border_map = numpy.zeros_like(padded_map, dtype=bool)
    border_todo = [padded_start_ij]
    while border_todo:
        this_border = border_todo.pop()
        region_map[*this_border] = True
        for n in (this_border + d for d in directions):  # always in bounds for padded map
            if padded_map[*n] == val and not region_map[*n]:
                border_todo.append(n)
            if padded_map[*n] != val:
                outside_border_map[*n] = True

    cropped_region_map = region_map[pad_size:-pad_size, pad_size:-pad_size]
    border_pad_size = pad_size-1
    cropped_border_map = outside_border_map[border_pad_size:-border_pad_size, border_pad_size:-border_pad_size]
    return cropped_region_map, cropped_border_map


def find_regions(map: numpy.ndarray, do_side_count=False) -> list[Region]:
    regions = []
    processed = numpy.zeros_like(map, dtype=bool)
    while True:
        unprocessed_plots = numpy.argwhere(processed == False)
        if len(unprocessed_plots) == 0:
            break

        region, _ = flood_region(map, start_ij := unprocessed_plots[0])
        processed[region] = True
        regions_indices = numpy.argwhere(region)
        num_sides = count_sides(region) if do_side_count else None
        regions.append(Region(map[*start_ij], len(regions_indices), find_perimeter(regions_indices), num_sides))

    return regions


def solve_part_1(raw_input):
    map = string_to_array(raw_input)
    regions = find_regions(map, do_side_count=False)
    return sum(r.size * r.perimeter for r in regions)
