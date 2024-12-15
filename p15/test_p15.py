from unittest import TestCase

from p15.p15 import parse, solve_part_1

demo_15_small = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""


class TestWarehouse(TestCase):
    def test_parse(self):
        warehouse, commands = parse(demo_15_small)
        self.assertEqual('@', warehouse.map[2, 2])
        self.assertEqual('<', commands[0])
        self.assertEqual('<', commands[-1])

    def test_step(self):
        warehouse, commands = parse(demo_15_small)

        for c in commands:
            warehouse.step(c)

        self.assertListEqual([4, 4], warehouse.robot_ij().tolist())

    def test_solve_demo_1_small(self):
        self.assertEqual(2028, solve_part_1(demo_15_small))
