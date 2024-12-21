from unittest import TestCase

from p21.p21 import shortest_key_sequences, directional_keypad, numeric_keypad, sequential_sequence, score_code


class Test(TestCase):
    def test_single_key_sequence(self):
        self.assertEqual(['<A'], shortest_key_sequences('0'))

    def test_two_button_sequence(self):
        self.assertEqual(['<A^A'], shortest_key_sequences('02'))

    def test_multiple_possibilities(self):
        sequences_1left_2up = shortest_key_sequences('5')
        self.assertEqual(3, len(sequences_1left_2up))
        self.assertIn('<^^A', sequences_1left_2up)
        self.assertIn('^<^A', sequences_1left_2up)
        self.assertIn('^^<A', sequences_1left_2up)

    def test_029A_keypad(self):
        sequences = shortest_key_sequences('029A')
        self.assertEqual(3, len(sequences))
        self.assertIn('<A^A^>^AvvvA', sequences)

    def test_directional_keypad(self):
        sequences = shortest_key_sequences('<A^A>^^AvvvA', directional_keypad)
        self.assertIn('v<<A>>^A<A>AvA<^AA>A<vAAA>^A', sequences)

    def test_sequential_keypads(self):
        keypads = numeric_keypad, directional_keypad

        outer_sequences = sequential_sequence('029A', keypads)

        self.assertIn('v<<A>>^A<A>AvA<^AA>A<vAAA>^A', outer_sequences)

    def test_score_code(self):
        self.assertEqual(68 * 29, score_code('029A'))
