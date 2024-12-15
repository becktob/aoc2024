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


class Warehouse2:
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

        to_move = self.things_to_move(self.robot_ij(), move)

        if to_move.size > 0:
            indexes_from = to_move.transpose()
            indexes_to = (to_move + (1, 0)).transpose()
            content = self.map[*indexes_from]
            self.map[*indexes_from] = ['.'] * to_move.shape[0]
            self.map[*indexes_to] = content

        self.map = numpy.rot90(self.map, -n_rot)

    def robot_ij(self):
        return numpy.argwhere(self.map == '@')[0]

    def boxes_ij(self):
        return numpy.argwhere(self.map == '[')

    def things_to_move(self, ij_push, move) -> numpy.ndarray:
        if self.map[*ij_push] == '#':
            return numpy.array([])

        all_moving_boxes = []

        moving_from_this_row = [ij_push]
        while True:
            for ij in moving_from_this_row[:]:
                if (val := self.map[*ij]) == '[' and move == 'v' or val == ']' and move == '^':
                    moving_from_this_row.append(ij + (0, 1))
                elif val == '[' and move == '^' or val == ']' and move == 'v':
                    moving_from_this_row.append(ij + (0, -1))

            all_moving_boxes.extend(moving_from_this_row)

            need_to_move_into_in_next_row = [m + (1, 0) for m in moving_from_this_row]
            if any('#' == self.map[*n] for n in need_to_move_into_in_next_row):
                return numpy.array([])

            boxes_need_to_move_next_row = [n for n in need_to_move_into_in_next_row if self.map[*n] in ('[', ']')]
            if len(boxes_need_to_move_next_row) == 0:
                return numpy.array(all_moving_boxes)

            moving_from_this_row = boxes_need_to_move_next_row


def parse2(raw_input) -> (Warehouse, list[str]):
    raw_warehouse, raw_commands = raw_input.split('\n\n')
    raw_warehouse = raw_warehouse.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    return Warehouse2(raw_warehouse), list(raw_commands.replace('\n', ''))


def solve_part_2(raw_input):
    warehouse, commands = parse2(raw_input)

    for c in commands:
        warehouse.step(c)

    return sum(100 * ij[0] + ij[1] for ij in warehouse.boxes_ij())
