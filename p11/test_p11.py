from unittest import TestCase

from p11.p11 import blink


class Test(TestCase):
    def test_blink_0_becomes_1(self):
        stones = list(blink([0]))
        self.assertListEqual([1], stones)
