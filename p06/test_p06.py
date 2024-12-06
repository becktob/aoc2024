from unittest import TestCase

from numpy.testing import assert_array_equal

from helpers import string_to_array
from p06.p06 import one_step

demo_input_6 = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

demo_6_step_5 = """....#.....
....^....#
....X.....
..#.X.....
....X..#..
....X.....
.#..X.....
........#.
#.........
......#...
"""


class Test(TestCase):
    def test_one_step_forward(self):
        maze = string_to_array(demo_input_6)
        maze_5 = string_to_array(demo_6_step_5)

        for _ in range(5):
            maze = one_step(maze)

        self.assertSequenceEqual(maze.tolist(), maze_5.tolist())

    def test_one_step_turn(self):
        maze = string_to_array(demo_input_6)
        maze_5 = string_to_array(demo_6_step_5)
        maze_6 = maze_5
        maze_6[maze_6 == '^'] = '>'

        for _ in range(6):
            maze = one_step(maze)

        self.assertSequenceEqual(maze.tolist(), maze_6.tolist())
