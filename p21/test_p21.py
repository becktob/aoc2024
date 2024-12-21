from unittest import TestCase

from p21.p21 import shortest_key_sequences


class Test(TestCase):
    def test_single_key_sequence(self):
        self.assertEqual(['<A'], shortest_key_sequences('0'))

    def test_two_button_sequence(self):
        self.assertEqual(['<A^A'], shortest_key_sequences('02'))
