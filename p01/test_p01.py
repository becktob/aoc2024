from unittest import TestCase

from p01.p01 import distances_of_smallest, solve_part_1, similarity_score, solve_part_2

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

    def test_solve_part_1(self):
        with open('p01/input') as f:
            self.assertEqual(1189304, solve_part_1(f.read()))

    def test_similarity_score(self):
        distances = similarity_score(demo_list_a, demo_list_b)
        self.assertEqual(31, distances)

    def test_solve_demo_2(self):
        self.assertEqual(31, solve_part_2(demo_input))

    def test_solve_part_2(self):
        with open('p01/input') as f:
            self.assertEqual(24349736, solve_part_2(f.read()))
