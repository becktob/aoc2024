from unittest import TestCase

from p25.p25 import parse_locks_keys, fit, solve_part_1

demo_input_25 = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""


class Test(TestCase):
    def test_parse_locks_keys(self):
        locks, keys = parse_locks_keys(demo_input_25)
        self.assertEqual(2, len(locks))
        self.assertEqual(3, len(keys))

        self.assertEqual((0, 5, 3, 4, 3), locks[0])
        self.assertEqual((4, 3, 4, 0, 2), keys[1])

    def test_fit(self):
        self.assertFalse(fit((0, 5, 3, 4, 3), (5, 0, 2, 1, 3)))
        self.assertTrue(fit((0, 5, 3, 4, 3), (3, 0, 2, 0, 1)))

    def test_solve_demo_1(self):
        self.assertEqual(3, solve_part_1(demo_input_25))

    def test_solve_part_1(self):
        with open('p25/input') as f:
            self.assertEqual(2993, solve_part_1(f.read()))
