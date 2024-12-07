from unittest import TestCase

from p07.p07 import can_make_true, solve_part_1, solve_part_2

demo_input_7 = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


class Test(TestCase):
    def test_can_make_true_two(self):
        self.assertTrue(can_make_true(190, [10, 19]))
        self.assertFalse(can_make_true(83, [17, 5]))

    def test_can_make_true_more(self):
        self.assertTrue(can_make_true(3267, [81, 40, 27]))
        self.assertTrue(can_make_true(292, [11, 6, 16, 20]))

    def test_solve_demo_1(self):
        self.assertEqual(3749, solve_part_1(demo_input_7))

    def test_solve_part_1(self):
        with open('p07/input') as f:
            self.assertEqual(1038838357795, solve_part_1(f.read()))

    def test_solve_demo_2(self):
        self.assertEqual(11387, solve_part_2(demo_input_7))
