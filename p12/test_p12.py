from unittest import TestCase

from helpers import string_to_array
from p12.p12 import find_areas

demo_input_12_1 = """AAAA
BBCD
BBCC
EEEC
"""


class Test(TestCase):
    def test_find_area_sizes(self):
        map = string_to_array(demo_input_12_1)
        areas = find_areas(map)
        sizes = [a.size for a in areas]
        self.assertListEqual([1, 3, 4, 4, 4], sorted(sizes))

    def test_find_area_perimeters(self):
        map = string_to_array(demo_input_12_1)
        areas = find_areas(map)
        perimeters = [a.perimeter for a in areas]
        self.assertListEqual([4, 8, 8, 10, 10], sorted(perimeters))
