from unittest import TestCase

from p03.p03 import find_mul, solve_part_1, solve_part_2

demo_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
demo_input_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


class Test(TestCase):
    def test_find_mul(self):
        self.assertEqual([(2, 4), (5, 5), (11, 8), (8, 5)], find_mul(demo_input))

    def test_solve_demo_1(self):
        self.assertEqual(161, solve_part_1(demo_input))

    def test_solve_part_1(self):
        with open('p03/input') as f:
            self.assertEqual(165225049, solve_part_1(f.read()))

    def test_solve_demo_2(self):
        self.assertEqual(48, solve_part_2(demo_input_2))

    def test_solve_part_2(self):
        with open('p03/input') as f:
            self.assertEqual(108830766, solve_part_2(f.read()))
