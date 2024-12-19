from unittest import TestCase

from p19.p19 import parse_towels_designs, find_combinations

demo_input_19 = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


class Test(TestCase):
    def test_parse_towels_designs(self):
        towels, designs = parse_towels_designs(demo_input_19)
        self.assertEqual(8, len(towels))
        self.assertEqual('wr', towels[1])
        self.assertEqual('brgr', designs[-2])

    def test_find_combination(self):
        towels, designs = parse_towels_designs(demo_input_19)
        self.assertIn(['br', 'wr', 'r'], find_combinations('brwrr', towels))

    def test_impossible_to_find_combination(self):
        towels, designs = parse_towels_designs(demo_input_19)
        self.assertEqual([], find_combinations('ubwu', towels))
