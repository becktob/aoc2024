import sys
from collections import defaultdict

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
        facing = self.facing == other.facing
        pos = self.pos_ij.tolist() == other.pos_ij.tolist()
        return facing and pos

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


class Maze:
    def __init__(self, raw_input):
        self.map = string_to_array(raw_input)
        self.end_ij = numpy.argwhere(self.map == 'E')[0]
        self.start_ij = numpy.argwhere(self.map == 'S')[0]

        self.paths_in_progress = []
        self.complete_paths = []

    def solve(self):
        starting_reindeer = Reindeer(self.start_ij, (0, 1))

        self.paths_in_progress = [[starting_reindeer]]
        costs_to_here: dict[Reindeer, int] = defaultdict(lambda: sys.maxsize)

        while self.paths_in_progress:
            path = self.paths_in_progress.pop(0)
            r = path[-1]

            if (r.pos_ij == self.end_ij).all():
                self.complete_paths.append(path)
                continue

            reindeer_forward = Reindeer(r.pos_ij + r.facing, r.facing)
            reindeer_left = Reindeer(r.pos_ij, r.left())
            reindeer_right = Reindeer(r.pos_ij, r.right())

            turned_last_step = len(path) > 1 and (path[-1].pos_ij == path[-2].pos_ij).all()
            possible_steps = (reindeer_forward,) if turned_last_step else (
                reindeer_forward, reindeer_left, reindeer_right)

            if False:
                debug = self.map.copy()
                for r in path:
                    debug[*r.pos_ij] = 'o'
                for s in possible_steps:
                    debug[*s.pos_ij] = s.symbol()

            for next_step in possible_steps:
                if self.map[*next_step.pos_ij] != '#' and next_step not in path:
                    extended_path = path + [next_step]
                    cost = path_cost(extended_path)
                    if cost > costs_to_here[next_step]:
                        continue
                    costs_to_here[next_step] = cost
                    self.paths_in_progress.append(extended_path)

        return self.complete_paths


def path_cost(path: list[Reindeer]):
    is_turn = [a.facing != b.facing for a, b in zip(path[1:], path[:-1])]

    turns = sum(1 for turn in is_turn if turn)
    steps = sum(1 for turn in is_turn if not turn)

    return 1000 * turns + 1 * steps


def solve_part_1(raw_input):
    maze = Maze(raw_input)
    paths = maze.solve()

    costs = [path_cost(p) for p in paths]
    return min(costs)
