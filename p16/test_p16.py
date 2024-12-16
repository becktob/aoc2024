import unittest
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

demo_input_16_2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""


class TestMaze(TestCase):
    def test_solve_demo_1(self):
        self.assertEqual(7036, solve_part_1(demo_input_16_1))

    def test_solve_demo_1_2(self):
        self.assertEqual(11048, solve_part_1(demo_input_16_2))

    @unittest.skip('slow')
    def test_solve_part_1(self):
        with open('p16/input') as f:
            self.assertEqual(1, solve_part_1(f.read()))
