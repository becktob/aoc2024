from unittest import TestCase

import numpy

from p04.p04 import string_to_array, find_xmases, find_straight_xmases, solve_part_1

demo_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

class TestP04(TestCase):
    def test_find_xmases(self):
        input = string_to_array(demo_input)
        xmases_found = list(find_xmases(input))
        for coords in xmases_found:
            input_display = numpy.ones_like(input)
            input_display.fill(' ')
            for c in coords:
                input_display[c] = input[c]
            #print(coords)
            #print(input_display)
        self.assertEqual(239,len(xmases_found))

    def test_find_straight_xmases(self):
        input = string_to_array(demo_input)
        xmases_found = list(find_straight_xmases(input))
        for coords in xmases_found:
            input_display = numpy.ones_like(input)
            input_display.fill(' ')
            for c in coords:
                input_display[c] = input[c]
            #print(coords)
            #print(input_display)
        self.assertEqual(18,len(xmases_found))

    def test_solve_part_1(self):
        with open('p04/input') as f:
            self.assertEqual(2642, solve_part_1(f.read()))
