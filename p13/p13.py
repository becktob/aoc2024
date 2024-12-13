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
        for n_a in range(100):
            loc_a = numpy.array(self.xy_a) * n_a
            for n_b in range(100):
                loc_b = numpy.array(self.xy_b) * n_b
                if all(loc_b + loc_a == self.xy_prize):
                    yield n_a, n_b

    def cheapest_solution_cost(self):
        solutions = self.solutions_ab()
        costs = (3*a + b for a,b in solutions)
        return min(costs)
