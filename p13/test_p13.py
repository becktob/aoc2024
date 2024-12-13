from unittest import TestCase

from p13.p13 import ClawMachine

raw_input_1 = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400"""
machine_1 = ClawMachine(raw_input_1)


class TestClawMachine(TestCase):
    def test_parse(self):
        self.assertEqual((94, 34), machine_1.xy_a)
        self.assertEqual((22, 67), machine_1.xy_b)
        self.assertEqual((8400, 5400), machine_1.xy_prize)

    def test_solutions_ab(self):
        solutions = list(machine_1.solutions_ab())
        self.assertIn((80, 40), solutions)

    def test_cheapest_solution(self):
        self.assertEqual(280, machine_1.cheapest_solution_cost())
