from unittest import TestCase

from p07.p07 import can_make_true


class Test(TestCase):
    def test_can_make_true_two(self):
        self.assertTrue(can_make_true(190, [10, 19]))
        self.assertFalse(can_make_true(83, [17, 5]))

    def test_can_make_true_more(self):
        self.assertTrue(can_make_true(3267, [81, 40, 27]))
        self.assertTrue(can_make_true(292, [11, 6 ,16, 20]))