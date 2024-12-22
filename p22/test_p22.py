from unittest import TestCase

from p22.p22 import evolve_secret_number, solve_part_1

demo_input_22 ="""1
10
100
2024"""

class Test(TestCase):
    def test_evolve_secret_number(self):
        self.assertEqual(15887950, evolve_secret_number(123))
        self.assertEqual(16495136, evolve_secret_number(15887950))

    def test_solve_demo_1(self):
        self.assertEqual(37327623, solve_part_1(demo_input_22))
