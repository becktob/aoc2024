from unittest import TestCase

from p09.p09 import DiskMap

demo_input_9 = "2333133121414131402"
demo_repr = "00...111...2...333.44.5555.6666.777.888899"


class TestDiskMap(TestCase):
    def test_parse_repr(self):
        map = DiskMap(demo_input_9)
        self.assertEqual(demo_repr, str(map))
