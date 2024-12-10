from unittest import TestCase

from p10.p10 import find_trails, trailhead_scores

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
        self.assertEqual(81, len(trails))  # TODO correct value?

    def test_trailhead_score(self):
        trails = list(find_trails(demo_input_10))
        self.assertEqual(36, trailhead_scores(trails))
