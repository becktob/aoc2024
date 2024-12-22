from unittest import TestCase

from p22.p22 import evolve_secret_number


class Test(TestCase):
    def test_evolve_secret_number(self):
        self.assertEqual(15887950, evolve_secret_number(123))
        self.assertEqual(16495136, evolve_secret_number(15887950))
