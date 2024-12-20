from unittest import TestCase

from p15.p15 import parse, solve_part_1, parse2, solve_part_2

demo_15_small = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

demo_15_part_2 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

demo_15_large = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


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

    def test_solve_part_1(self):
        with open('p15/input') as f:
            self.assertEqual(1318523, solve_part_1(f.read()))


class TestWarehouse2(TestCase):
    def test_parse(self):
        warehouse, commands = parse2(demo_15_part_2)
        self.assertEqual('@', warehouse.map[3, 10])
        self.assertEqual('<', commands[0])

    def test_step(self):
        warehouse, commands = parse2(demo_15_part_2)

        for c in commands:
            warehouse.step(c)

        self.assertListEqual([2, 5], warehouse.robot_ij().tolist())


    def test_solve_demo_2_large(self):
        self.assertEqual(9021, solve_part_2(demo_15_large))

    def test_solve_part_2(self):
        with open('p15/input') as f:
            self.assertEqual(1337648, solve_part_2(f.read()))
