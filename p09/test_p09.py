import unittest
from unittest import TestCase

from p09.p09 import DiskMap, solve_part_1, DiskMap2, solve_part_2

demo_input_9 = "2333133121414131402"
demo_repr = "00...111...2...333.44.5555.6666.777.888899"


class TestDiskMap(TestCase):
    def test_parse_repr(self):
        map = DiskMap(demo_input_9)
        self.assertEqual(demo_repr, str(map))

    def test_compact_one_stepp(self):
        map = DiskMap(demo_input_9)

        map.compact_one_step()
        step_1 = "009..111...2...333.44.5555.6666.777.88889."
        self.assertEqual(step_1, str(map))

        map.compact_one_step()
        step_2 = "0099.111...2...333.44.5555.6666.777.8888.."
        self.assertEqual(step_2, str(map))

    def test_compact_all(self):
        map = DiskMap(demo_input_9)
        map.compact_all()

        step_n = "0099811188827773336446555566.............."
        self.assertEqual(step_n, str(map))

    def test_solve_demo_part1(self):
        solve_part_1(demo_input_9)

    @unittest.skip("slow")
    def test_solve_part_1(self):
        with open('p09/input') as f:
            self.assertEqual(6241633730082, solve_part_1(f.read()))


class TestDiskMap2(TestCase):
    def test_parse_repr(self):
        map = DiskMap2(demo_input_9)
        self.assertEqual(demo_repr, str(map))

    def test_compact_all(self):
        map = DiskMap2(demo_input_9)
        map.compact_all()

        step_n = "00992111777.44.333....5555.6666.....8888.."
        self.assertEqual(step_n, str(map))

    def test_solve_demo_part2(self):
        self.assertEqual(2858, solve_part_2(demo_input_9))
