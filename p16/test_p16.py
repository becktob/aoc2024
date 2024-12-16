from unittest import TestCase

from p16.p16 import solve_part_1

demo_input_16_1 = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


class TestMaze(TestCase):
    def test_solve_demo_1(self):
        self.assertEqual(7036, solve_part_1(demo_input_16_1))
