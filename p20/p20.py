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
            if t_start % 100 == 0:
                print(f"{t_start}/{len(path)}")
            for t_skip, cheat_end in enumerate(path[t_start + min_save + 2:]):
                if sum(abs(cheat_end - cheat_start)) == 2:
                    time_saved = t_skip + min_save
                    cheats.append(((cheat_start, cheat_end), time_saved))

        return cheats


def solve_part_1(raw_input):
    racetrack = Racetrack(raw_input)
    return len(racetrack.find_cheats(100))
