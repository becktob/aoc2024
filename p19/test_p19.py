from unittest import TestCase

from p19.p19 import parse_towels_designs, find_combinations, solve_part_1, can_combine, solve_part_2, count_combine

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

    def test_can_combine(self):
        towels, designs = parse_towels_designs(demo_input_19)
        self.assertTrue(can_combine('brwrr', towels))
        self.assertTrue(can_combine('bwurrg', towels))
        self.assertFalse(can_combine('ubwu', towels))

    def test_solve_demo_1(self):
        self.assertEqual(6, solve_part_1(demo_input_19))

    def test_solve_part1(self):
        with open('p19/input') as f:
            self.assertEqual(258, solve_part_1(f.read()))

    def test_solve_demo_2(self):
        self.assertEqual(16, solve_part_2(demo_input_19))
