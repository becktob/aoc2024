from unittest import TestCase

from p11.p11 import blink, solve_part_1


class Test(TestCase):
    def test_blink_0_becomes_1(self):
        stones = list(blink([0]))
        self.assertListEqual([1], stones)

    def test_demo_first_step(self):
        stones = list(blink([125, 17]))
        self.assertListEqual([253000, 1, 7], stones)

    def test_solve_demo_1(self):
        self.assertEqual(55312, solve_part_1("125 17"))

    def test_solve_part_1(self):
        with open('p11/input') as f:
            self.assertEqual(217812, solve_part_1(f.read()))

    def test_solve_part_2(self):
        with open('p11/input') as f:
            self.assertEqual(259112729857522, solve_part_1(f.read(), num_blinks=75))
