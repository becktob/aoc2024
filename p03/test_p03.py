from unittest import TestCase

from p03.p03 import find_mul, solve_part_1

demo_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


class Test(TestCase):
    def test_find_mul(self):
        self.assertEqual([(2, 4), (5, 5), (11, 8), (8, 5)], find_mul(demo_input))

    def test_solve_part_1(self):
        self.assertEqual(161, solve_part_1(demo_input))
