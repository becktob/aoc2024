import sys
from collections import defaultdict
from functools import cache

import numpy

from helpers import string_to_array

directions = {'^': (-1, 0),
              '>': (0, +1),
              'v': (+1, 0),
              '<': (0, -1)}
symbols = {v: k for k, v in directions.items()}


class Reindeer:
    directions_rightwise = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def __init__(self, pos_ij, facing):
        self.pos_ij = pos_ij
        self.facing = facing

    def __repr__(self):
        return f'<R: {self.pos_ij.tolist()}, [{self.symbol()}]>'

    def __eq__(self, other):
        if not isinstance(other, Reindeer):
            return False
        return self.facing == other.facing and self.pos_ij[0] == other.pos_ij[0] and self.pos_ij[1] == other.pos_ij[1]

    def __hash__(self):
        return hash((tuple(self.pos_ij), self.facing))

    def right(self):  # Todo: name?
        i = Reindeer.directions_rightwise.index(self.facing)
        return Reindeer.directions_rightwise[(i + 1) % 4]

    def left(self):
        i = Reindeer.directions_rightwise.index(self.facing)
        return Reindeer.directions_rightwise[(i - 1) % 4]

    def symbol(self):
        return symbols[self.facing]


@cache
class Maze:
    def __init__(self, raw_input):
        self.map = string_to_array(raw_input)
        self.end_ij = numpy.argwhere(self.map == 'E')[0]
        self.start_ij = numpy.argwhere(self.map == 'S')[0]

        self.paths_in_progress = []
        self.costs_in_progress = []
        self.complete_paths = []

    @cache
    def solve(self):
        starting_reindeer = Reindeer(self.start_ij, (0, 1))

        self.paths_in_progress = [[starting_reindeer]]
        # a bit flaky: two parallel lists. But: "... in paths_in_progress' seems cheaper this way
        self.costs_in_progress = [0]
        costs_to_here: dict[Reindeer, int] = defaultdict(lambda: sys.maxsize)

        while self.paths_in_progress:
            path = self.paths_in_progress.pop(0)
            cost = self.costs_in_progress.pop(0)
            r = path[-1]

            if cost > costs_to_here[r]:
                continue

            if (r.pos_ij == self.end_ij).all():
                self.complete_paths.append((cost, path))
                continue

            reindeer_forward = Reindeer(r.pos_ij + r.facing, r.facing)
            reindeer_left = Reindeer(r.pos_ij + (face_left := r.left()), face_left)
            reindeer_right = Reindeer(r.pos_ij + (face_right := r.right()), face_right)

            turned_last_step = len(path) > 1 and (path[-1].pos_ij == path[-2].pos_ij).all()
            possible_steps = [(reindeer_forward, 1)]
            if not turned_last_step:
                possible_steps.append((reindeer_left, 1001))
                possible_steps.append((reindeer_right, 1001))

            for next_step, add_cost in possible_steps:
                if self.map[*next_step.pos_ij] != '#' and next_step not in path:
                    extended_path = path + [next_step]
                    extended_cost = cost + add_cost
                    if extended_cost > costs_to_here[next_step]:
                        continue
                    costs_to_here[next_step] = extended_cost
                    self.paths_in_progress.append(extended_path)
                    self.costs_in_progress.append(extended_cost)

        return self.complete_paths


def solve_part_1(raw_input):
    maze = Maze(raw_input)
    costs, paths = zip(*maze.solve())
    return min(costs)


def solve_part_2(raw_input):
    maze = Maze(raw_input)
    cost_paths = maze.solve()

    lowest_cost = min(c for c, _ in cost_paths)
    cheapest_paths = [p for c, p in cost_paths if c == lowest_cost]

    locations = set()
    for path in cheapest_paths:
        locations.update(tuple(r.pos_ij) for r in path)

    return len(locations)
