from unittest import TestCase

from p13.p13 import ClawMachine, solve_part_1, solve_part_2

raw_input_1 = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400"""
machine_1 = ClawMachine(raw_input_1)

demo_input_13 = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


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

    def test_solve_demo_1(self):
        self.assertEqual(480, solve_part_1(demo_input_13))

    def test_solve_part_1(self):
        with open('p13/input') as f:
            self.assertEqual(28753, solve_part_1(f.read()))

    def test_solve_demo_2(self):
        self.assertEqual(875318608908, solve_part_2(demo_input_13))

    def test_solve_part_2(self):
        with open('p13/input') as f:
            self.assertEqual(102718967795500, solve_part_2(f.read()))
