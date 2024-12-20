from unittest import TestCase

from p20.p20 import Racetrack

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
