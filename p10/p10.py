from collections import defaultdict

import numpy

import helpers
from helpers import in_bounds


def find_trails(raw_input):
    height_map = helpers.string_to_array(raw_input, mapper=int)

    trails_in_progress = [[head] for head in numpy.argwhere(height_map == 0)]

    while trails_in_progress:
        trail = trails_in_progress.pop()
        tail = trail[-1]

        if 9 == height_map[*tail]:
            yield trail
            continue

        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
        next_positions = [tail + s for s in steps]
        in_bounds_positions = list(p for p in next_positions if in_bounds(p, height_map))
        inc_by_1_positions = list(p for p in in_bounds_positions if height_map[*tail] + 1 == height_map[*p])

        trails_in_progress += [trail + [p] for p in inc_by_1_positions]


def trailhead_scores(trails):
    trailheads = defaultdict(set)
    for trail in trails:
        trailheads[tuple(trail[0])].add(tuple(trail[-1]))

    return sum((len(ends) for ends in trailheads.values()))


def solve_part_1(raw_input):
    trails = find_trails(raw_input)
    return trailhead_scores(trails)
