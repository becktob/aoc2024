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

        robot_ij = self.robot_ij()

        slice_i = slice(robot_ij[0], None, direction[0]) if direction[0] else robot_ij[0]
        slice_j = slice(robot_ij[1], None, direction[1]) if direction[1] else robot_ij[1]

        # only tiles [robot...wall] can change -> make problem 1d
        robot_to_wall = "".join(self.map[slice_i, slice_j])

        first_wall = robot_to_wall.find('#')
        first_space = robot_to_wall.find('.')

        robot_can_move = 0 < first_space < first_wall
        if robot_can_move:
            moved = robot_to_wall[0:first_space]
            remains = robot_to_wall[first_space + 1:]
            robot_to_wall_after = '.' + moved + remains

            self.map[slice_i, slice_j] = list(robot_to_wall_after)

    def robot_ij(self):
        return numpy.argwhere(self.map == '@')[0]

    def boxes_ij(self):
        return numpy.argwhere(self.map == 'O')


def parse(raw_input) -> (Warehouse, list[str]):
    raw_warehouse, raw_commands = raw_input.split('\n\n')
    return Warehouse(raw_warehouse), list(raw_commands.replace('\n',''))


def solve_part_1(raw_input):
    warehouse, commands = parse(raw_input)

    for c in commands:
        warehouse.step(c)

    return sum(100 * ij[0] + ij[1] for ij in warehouse.boxes_ij())
