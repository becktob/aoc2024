from unittest import TestCase

from p13.p13 import ClawMachine


class TestClawMachine(TestCase):
    def test_parse(self):
        raw_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400"""
        machine = ClawMachine(raw_input)

        self.assertEqual((94, 34), machine.xy_a)
        self.assertEqual((22, 67), machine.xy_b)
        self.assertEqual((8400, 5400), machine.xy_prize)

    def test_solutions_ab(self):
        raw_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400"""
        machine = ClawMachine(raw_input)

        solutions = list(machine.solutions_ab())
        self.assertIn((80, 40), solutions)
