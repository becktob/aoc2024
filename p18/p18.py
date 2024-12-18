import sys
from collections import defaultdict


class Ram:
    def __init__(self, raw_input: str, num_bytes: int, size: int = None):
        self.corrupted = [tuple(int(xy) for xy in l.split(',')) for l in raw_input.splitlines()]
        self.corrupted = self.corrupted[:num_bytes]
        self.size = size
        if size is None:
            self.size = max(xy for c in self.corrupted for xy in c)

    def flood_from_exit(self):
        steps_to_exit = defaultdict(lambda: sys.maxsize)
        steps_to_exit[exit := (self.size, self.size)] = 0
        xy_in_progress = [exit]

        while xy := xy_in_progress.pop(0) if xy_in_progress else None is not None:
            steps_to_here = steps_to_exit[xy]

            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                xy_next = tuple(c + d for c, d in zip(xy, d))
                if any(not 0 <= xy <= self.size for xy in xy_next):
                    continue
                if xy in self.corrupted:
                    continue

                if (steps_to_next := steps_to_here + 1) < steps_to_exit[xy_next]:
                    steps_to_exit[xy_next] = steps_to_next
                    xy_in_progress.append(xy_next)

        return steps_to_exit[(0, 0)]


def solve_part_1(raw_input, num_bytes):
    ram = Ram(raw_input, num_bytes)
    return ram.flood_from_exit()


def solve_part_2(raw_input):
    lines = raw_input.splitlines()
    corrupted = [tuple(int(xy) for xy in l.split(',')) for l in raw_input.splitlines()]
    size = max(xy for c in corrupted for xy in c)

    num_under, num_over = 0, len(lines)

    while num_under < (num_middle := (num_under + num_over) // 2) < num_over:
        if Ram(raw_input, num_middle, size).flood_from_exit() == sys.maxsize:
            num_over = num_middle
        else:
            num_under = num_middle

    return lines[num_under]
