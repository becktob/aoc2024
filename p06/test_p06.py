from unittest import TestCase

from numpy.testing import assert_array_equal

from helpers import string_to_array
from p06.p06 import one_step, solve

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
            maze, _ = one_step(maze)

        self.assertSequenceEqual(maze.tolist(), maze_5.tolist())

    def test_one_step_turn(self):
        maze = string_to_array(demo_input_6)
        maze_5 = string_to_array(demo_6_step_5)
        maze_6 = maze_5
        maze_6[maze_6 == '^'] = '>'

        for _ in range(6):
            maze, _ = one_step(maze)

        self.assertSequenceEqual(maze.tolist(), maze_6.tolist())

    def test_solve_demo_part_1(self):
        self.assertEqual(41, solve(demo_input_6))

    def test_solve_part_1(self):
        with open('p06/input') as f:
            self.assertEqual(4696, solve(f.read()))
