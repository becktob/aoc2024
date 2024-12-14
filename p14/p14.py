import operator
import re
from functools import reduce


class Robot:
    def __init__(self, raw_line: str):
        m = re.match("p=(.*) v=(.*)", raw_line)
        self.p_xy = tuple(int(xy) for xy in m.group(1).split(','))
        self.v_xy = tuple(int(xy) for xy in m.group(2).split(','))

    def __repr__(self):
        return f"<Robot at {self.p_xy}>"

    def move(self, steps: int, room_size: tuple[int, int]):
        self.p_xy = tuple((p + steps * v) % s for p, v, s in zip(self.p_xy, self.v_xy, room_size))

    @property
    def x(self):
        return self.p_xy[0]

    @property
    def y(self):
        return self.p_xy[1]


def solve_part_1(raw_input: str, room_size=(101, 103)):
    steps = 100
    robots = [Robot(r) for r in raw_input.splitlines()]

    [r.move(steps, room_size) for r in robots]

    x_half = room_size[0] // 2
    y_half = room_size[1] // 2
    nw = [r for r in robots if 0 <= r.x < x_half and 0 <= r.y < y_half]
    ne = [r for r in robots if x_half < r.x and 0 <= r.y < y_half]
    sw = [r for r in robots if 0 <= r.x < x_half and y_half < r.y]
    se = [r for r in robots if x_half < r.x and y_half < r.y]

    return reduce(operator.mul, map(len, (nw, ne, sw, se)), 1)
