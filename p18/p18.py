import sys
from collections import defaultdict


class Ram:
    def __init__(self, raw_input: str, num_bytes: int):
        self.corrupted = [tuple(int(xy) for xy in l.split(',')) for l in raw_input.splitlines()]
        self.corrupted = self.corrupted[:num_bytes]
        self.size = max(xy for c in self.corrupted for xy in c)

    def flood_from_exit(self):
        exit = (self.size, self.size)
        steps_to_exit = defaultdict(lambda: sys.maxsize)
        steps_to_exit[exit] = 0
        xy_in_progress = [exit]

        while xy := xy_in_progress.pop(0) if xy_in_progress else None is not None:
            steps_to_here = steps_to_exit[xy]
            steps_to_next = steps_to_here + 1

            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                xy_next = tuple(c + d for c, d in zip(xy, d))
                if any(not 0 <= xy <= self.size for xy in xy_next):
                    continue
                if xy in self.corrupted:
                    continue

                if steps_to_next < steps_to_exit[xy_next]:
                    steps_to_exit[xy_next] = steps_to_next
                    xy_in_progress.append(xy_next)

        return steps_to_exit[(0, 0)]


def solve_part_1(raw_input, num_bytes):
    ram = Ram(raw_input, num_bytes)
    return ram.flood_from_exit()
