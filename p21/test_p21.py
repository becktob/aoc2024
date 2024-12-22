from unittest import TestCase

from p21.p21 import shortest_key_sequences, directional_keypad, numeric_keypad, sequential_sequence, score_code, \
    solve_part_1, shortest_button_to_button, solve_part_2, score_code_count_only, count_shortest_button_to_button

demo_input_21 = """029A
980A
179A
456A
379A
"""


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

    def test_multiple_possibilities_simple_only(self):
        sequences_1left_2up = shortest_key_sequences('5', simple_only=True)
        self.assertEqual(2, len(sequences_1left_2up))
        self.assertIn('<^^A', sequences_1left_2up)
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

        outer_sequences = sequential_sequence('0', keypads)
        self.assertIn('v<<A>>^A', outer_sequences)

    def test_button_to_button(self):
        pads = numeric_keypad, directional_keypad, directional_keypad

        self.assertIn('<A', shortest_button_to_button('A', '0', pads[:1]))
        self.assertIn('v<<A>>^A', shortest_button_to_button('A', '0', pads[:2]))
        self.assertIn('<vA<AA>>^AvAA<^A>A', shortest_button_to_button('A', '0', pads[:3]))

    def test_score_code(self):
        for score, code in ((68 * 29, '029A'),
                            (60 * 980, '980A'),
                            (68 * 179, '179A'),
                            (64 * 456, '456A'),
                            (64 * 379, '379A')
                            ):
            with self.subTest(code):
                self.assertEqual(score, score_code(code))

    def test_score_code_count_only(self):
        for score, code in ((68 * 29, '029A'),
                            (60 * 980, '980A'),
                            (68 * 179, '179A'),
                            (64 * 456, '456A'),
                            (64 * 379, '379A')
                            ):
            with self.subTest(code):
                self.assertEqual(score, score_code_count_only(code))

    def test_solve_demo(self):
        self.assertEqual(126384, solve_part_1(demo_input_21))

    def test_solve_part_1(self):
        with open('p21/input') as f:
            self.assertEqual(213536, solve_part_1(f.read()))

    def test_solve_part_2(self):
        with open('p21/input') as f:
            self.assertEqual(258369757013802, solve_part_2(f.read()))

        print(count_shortest_button_to_button.cache_info())
