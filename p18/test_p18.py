from unittest import TestCase

from p18.p18 import Ram, solve_part_1, solve_part_2

demo_input_18 = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


class TestRam(TestCase):
    def test_parse(self):
        ram = Ram(demo_input_18, 12)
        self.assertEqual(6, ram.size)

    def test_solve_demo_1(self):
        self.assertEqual(22, solve_part_1(demo_input_18, 12))

    def test_solve_part_1(self):
        with open('p18/input') as f:
            self.assertEqual(336, solve_part_1(f.read(), 1024))

    def test_solve_demo_2(self):
        self.assertEqual("6,1", solve_part_2(demo_input_18))

    def test_solve_part_2(self):
        with open('p18/input') as f:
            self.assertEqual("24,30", solve_part_2(f.read()))
