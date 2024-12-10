from unittest import TestCase

from p10.p10 import find_trails, trailhead_scores, solve_part_1, solve_part_2

demo_input_10 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


class Test(TestCase):
    def test_find_trails(self):
        trails = list(find_trails(demo_input_10))
        self.assertEqual(81, len(trails))

    def test_trailhead_score(self):
        trails = list(find_trails(demo_input_10))
        self.assertEqual(36, trailhead_scores(trails))

    def test_solve_demo_1(self):
        self.assertEqual(36, solve_part_1(demo_input_10))

    def test_solve_part_1(self):
        with open('p10/input') as f:
            self.assertEqual(682, solve_part_1(f.read()))

    def test_solve_demo_2(self):
        self.assertEqual(81, solve_part_2(demo_input_10))

    def test_solve_part_2(self):
        with open('p10/input') as f:
            self.assertEqual(1511, solve_part_2(f.read()))
