from unittest import TestCase

from p04.p04 import string_to_array, find_xmases

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
        find_xmases(input)
