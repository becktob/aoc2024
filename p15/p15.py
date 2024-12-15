import numpy

from helpers import string_to_array


class Warehouse:
    # i,j (line, col) indexing
    def __init__(self, map_string: str):
        self.map = string_to_array(map_string)

    def step(self, move: str):
        direction_chars = {'v': (1, 0),
                           '^': (-1, 0),
                           '>': (0, 1),
                           '<': (0, -1)}
        direction = direction_chars[move]

        robot_ij = numpy.argwhere(self.map == '@')[0]

        slice_i = slice(robot_ij[0], None, direction[0]) if direction[0] else robot_ij[0]
        slice_j = slice(robot_ij[1], None, direction[1]) if direction[1] else robot_ij[1]
        robot_to_wall = self.map[slice_i, slice_j]
        print(robot_to_wall)


def parse(raw_input) -> (Warehouse, list[str]):
    raw_warehouse, raw_commands = raw_input.split('\n\n')
    return Warehouse(raw_warehouse), list(raw_commands.strip())
