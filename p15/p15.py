import numpy

from helpers import string_to_array


class Warehouse:
    # i,j (line, col) indexing
    def __init__(self, map_string: str):
        self.map = string_to_array(map_string)

    def step(self, move: str):
        rot90_so_motion_is_down = {'v': 0,
                                   '^': 2,
                                   '>': 3,
                                   '<': 1}
        n_rot = rot90_so_motion_is_down[move]
        self.map = numpy.rot90(self.map, n_rot)

        robot_ij = self.robot_ij()

        # only tiles [robot...wall] can change -> make problem 1d
        robot_to_wall = "".join(self.map[robot_ij[0]:, robot_ij[1]])

        first_wall = robot_to_wall.find('#')
        first_space = robot_to_wall.find('.')

        robot_can_move = 0 < first_space < first_wall
        if robot_can_move:
            moved = robot_to_wall[0:first_space]
            remains = robot_to_wall[first_space + 1:]
            robot_to_wall_after = '.' + moved + remains

            self.map[robot_ij[0]:, robot_ij[1]] = list(robot_to_wall_after)

        self.map = numpy.rot90(self.map, -n_rot)

    def robot_ij(self):
        return numpy.argwhere(self.map == '@')[0]

    def boxes_ij(self):
        return numpy.argwhere(self.map == 'O')


def parse(raw_input) -> (Warehouse, list[str]):
    raw_warehouse, raw_commands = raw_input.split('\n\n')
    return Warehouse(raw_warehouse), list(raw_commands.replace('\n', ''))


def solve_part_1(raw_input):
    warehouse, commands = parse(raw_input)

    for c in commands:
        warehouse.step(c)

    return sum(100 * ij[0] + ij[1] for ij in warehouse.boxes_ij())
