from unittest import TestCase

from p21.p21 import shortest_key_sequences


class Test(TestCase):
    def test_single_key_sequence(self):
        self.assertEqual(['<A'], shortest_key_sequences('0'))
