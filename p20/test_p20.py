from unittest import TestCase

from p20.p20 import Racetrack, solve_part_1

demo_input_20 = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""


class TestRacetrack(TestCase):
    def test_find_track(self):
        racetrack = Racetrack(demo_input_20)
        path = racetrack.find_path()
        self.assertEqual(84, len(path) - 1)

    def test_find_cheats(self):
        racetrack = Racetrack(demo_input_20)
        cheats = racetrack.find_cheats(20)
        self.assertEqual(5, len(cheats))

    def test_full_track_part_1(self):
        with open('p20/input') as f:
            racetrack = Racetrack(f.read())
            path = racetrack.find_path()
            self.assertEqual(9448, len(path) - 1)

    def test_solve_part_1(self):
        with open('p20/input') as f:
            self.assertEqual(1387, solve_part_1(f.read()))
