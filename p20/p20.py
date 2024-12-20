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

    def find_cheats(self, min_save):
        path = self.find_path()

        cheats = []
        for t_start, cheat_start in enumerate(path):
            for t_end, cheat_end in enumerate(path):
                if sum(abs(cheat_end - cheat_start)) == 2:
                    time_saved = t_end - t_start - 2
                    cheats.append(((cheat_start, cheat_end), time_saved))

        return [c for c in cheats if c[1] >= min_save]
