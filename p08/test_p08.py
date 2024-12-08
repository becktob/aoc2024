from unittest import TestCase

import numpy

from helpers import string_to_array
from p08.p08 import antinodes, solve_part_1, solve_part_2

demo_input_8 = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

example_input_8 = """..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
..........
"""


class Test(TestCase):
    def test_example(self):
        map = string_to_array(example_input_8)
        antinode_map = antinodes(map)
        antinode_count = numpy.count_nonzero(antinode_map)
        self.assertEqual(2, antinode_count)

    def test_demo_part_1(self):
        antinode_count = solve_part_1(demo_input_8)
        self.assertEqual(14, antinode_count)

    def test_solve_part_1(self):
        with open('p08/input') as f:
            self.assertEqual(323, solve_part_1(f.read()))

    def test_demo_part_2(self):
        antinode_count = solve_part_2(demo_input_8)
        self.assertEqual(34, antinode_count)

    def test_solve_part_2(self):
        with open('p08/input') as f:
            self.assertEqual(1077, solve_part_2(f.read()))
