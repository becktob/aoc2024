from unittest import TestCase

from p07.p07 import can_make_true


class Test(TestCase):
    def test_can_make_true(self):
        self.assertTrue(can_make_true(190, [10, 19]))
        self.assertFalse(can_make_true(83, [17, 5]))
