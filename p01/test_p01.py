from unittest import TestCase

from p01.p01 import distances_of_smallest, solve_part_1

demo_input = """3   4
4   3
2   5
1   3
3   9
3   3
"""

demo_list_a, demo_list_b = zip(*(map(int, line.split()) for line in demo_input.splitlines()))


class Test(TestCase):
    def test_distances_of_smallest(self):
        distances = distances_of_smallest(demo_list_a, demo_list_b)
        self.assertEqual([2, 1, 0, 1, 2, 5], distances)

    def test_solve_demo_1(self):
        self.assertEqual(11, solve_part_1(demo_input))
