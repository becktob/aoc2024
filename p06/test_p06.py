import unittest
from unittest import TestCase

from helpers import string_to_array
from p06.p06 import one_step, solve_part_1, is_loop, solve_part_2, find_start

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

        state = find_start(maze)
        for _ in range(5):
            state = one_step(maze, state)

        self.assertEqual(((1, 4), '^'), state)

    def test_one_step_turn(self):
        maze = string_to_array(demo_input_6)

        state = find_start(maze)
        for _ in range(6):
            state = one_step(maze, state)

        self.assertEqual(((1, 4), '>'), state)

    def test_solve_demo_part_1(self):
        self.assertEqual(41, solve_part_1(demo_input_6))

    def test_solve_part_1(self):
        with open('p06/input') as f:
            self.assertEqual(4696, solve_part_1(f.read()))

    def test_is_not_loop(self):
        maze = string_to_array(demo_input_6)
        self.assertFalse(is_loop((maze)))

    def test_is_loop(self):
        maze = string_to_array(demo_input_6)
        maze[6, 3] = '#'
        self.assertTrue(is_loop((maze)))

    def test_solve_demo_2(self):
        self.assertEqual(6, solve_part_2(demo_input_6))

    @unittest.skip("slow")
    def test_solve_part_2(self):
        with open('p06/input') as f:
            self.assertEqual(1443, solve_part_2(f.read()))
