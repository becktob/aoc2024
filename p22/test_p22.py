from unittest import TestCase

from p22.p22 import evolve_secret_number, solve_part_1, sale_from_sequence, solve_part_2

demo_input_22 = """1
10
100
2024"""

demo_input_22_2 = """1
2
3
2024"""


class Test(TestCase):
    def test_evolve_secret_number(self):
        self.assertEqual(15887950, evolve_secret_number(123))
        self.assertEqual(16495136, evolve_secret_number(15887950))

    def test_solve_demo_1(self):
        self.assertEqual(37327623, solve_part_1(demo_input_22))

    def test_solve_part_1(self):
        with open('p22/input') as f:
            self.assertEqual(12979353889, solve_part_1(f.read()))

    def test_sale_from_sequence(self):
        sequence = (-2, 1, -1, 3)
        self.assertEqual(7, sale_from_sequence(1, sequence))
        self.assertEqual(7, sale_from_sequence(2, sequence))
        self.assertEqual(None, sale_from_sequence(3, sequence))
        self.assertEqual(9, sale_from_sequence(2024, sequence))

    def test_solve_demo_2(self):
        self.assertEqual((-2, 1, -1, 3), solve_part_2(demo_input_22_2))
