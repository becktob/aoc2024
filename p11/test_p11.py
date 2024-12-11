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
