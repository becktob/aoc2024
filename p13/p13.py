import re

import numpy


def parse_xy(raw_button):
    m = re.match('.*: X=?(.*?), Y=?(.*)', raw_button)
    return tuple(int(xy) for xy in (m.group(1), m.group(2)))


class ClawMachine:
    def __init__(self, raw_input):
        raw_a, raw_b, raw_prize = raw_input.split('\n')

        self.xy_a = parse_xy(raw_a)
        self.xy_b = parse_xy(raw_b)
        self.xy_prize = parse_xy(raw_prize)

    def solutions_ab(self):
        px, py = self.xy_prize
        ax, ay = self.xy_a
        bx, by = self.xy_b

        n_a = (by * px - bx * py) // (by * ax - bx * ay)
        n_b = - (ay * px - ax * py) // (by * ax - bx * ay)

        if n_a * ax + n_b * bx == px and n_a * ay + n_b * by == py:
            return ((n_a, n_b),)
        else:
            return ()

    def cheapest_solution_cost(self):
        solutions = self.solutions_ab()
        costs = (3 * a + b for a, b in solutions)
        return min(costs, default=0)


def solve_part_1(raw_input):
    raw_machines = raw_input.strip().split('\n\n')
    machines = [ClawMachine(r) for r in raw_machines]

    return sum(m.cheapest_solution_cost() for m in machines)


def solve_part_2(raw_input):
    raw_machines = raw_input.strip().split('\n\n')
    machines = [ClawMachine(r) for r in raw_machines]
    for m in machines:
        m.xy_prize = tuple(xy + 10000000000000 for xy in m.xy_prize)

    return sum(m.cheapest_solution_cost() for m in machines)
