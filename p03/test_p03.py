from unittest import TestCase

from p03.p03 import find_mul

demo_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


class Test(TestCase):
    def test_find_mul(self):
        self.assertEqual([(2, 4), (5, 5), (11, 8), (8, 5)], find_mul(demo_input))
