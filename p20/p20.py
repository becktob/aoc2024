import numpy

from helpers import string_to_array


class Racetrack:
    def __init__(self, raw_input):
        self.map = string_to_array(raw_input)

    def find_path(self):
        start = numpy.argwhere(self.map == 'S')[0]

        path = [start]
        while True:
            tail = path[-1]
            neighbors = [tail + d for d in ((0, 1), (0, -1), (1, 0), (-1, 0))]

            next_step = [n for n in neighbors if self.map[*n] in ('.', 'E')]
            if len(path) > 1:
                next_step = [n for n in next_step if not (n == path[-2]).all()]

            path.append(next_step[0])

            if self.map[*next_step[0]] == 'E':
                break

        return path
