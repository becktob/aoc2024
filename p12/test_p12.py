import unittest
from unittest import TestCase

from helpers import string_to_array
from p12.p12 import find_regions, solve_part_1, solve_part_2

demo_input_12_1 = """AAAA
BBCD
BBCC
EEEC
"""

demo_input_12_3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


class Test(TestCase):
    def test_find_region_sizes(self):
        map = string_to_array(demo_input_12_1)
        regions = find_regions(map)
        sizes = [r.size for r in regions]
        self.assertListEqual([1, 3, 4, 4, 4], sorted(sizes))

    def test_find_region_perimeters(self):
        map = string_to_array(demo_input_12_1)
        regions = find_regions(map)
        perimeters = [r.perimeter for r in regions]
        self.assertListEqual([4, 8, 8, 10, 10], sorted(perimeters))

    def test_solve_demo_1_1(self):
        self.assertEqual(140, solve_part_1(demo_input_12_1))

    def test_solve_demo_1_3(self):
        self.assertEqual(1930, solve_part_1(demo_input_12_3))

    @unittest.skip('slow')
    def test_solve_part_1(self):
        with open('p12/input') as f:
            self.assertEqual(1363484, solve_part_1(f.read()))

    def test_count_sides(self):
        map = string_to_array(demo_input_12_1)
        regions = find_regions(map, True)
        sides = [r.sides for r in regions]
        self.assertListEqual([4, 4, 4, 4, 8], sorted(sides))

    def test_demo_2_3(self):
        self.assertEqual(1206, solve_part_2(demo_input_12_3))

    def test_solve_part_2(self):
        with open('p12/input') as f:
            self.assertEqual(838988, solve_part_2(f.read()))
