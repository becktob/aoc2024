from unittest import TestCase

from p18.p18 import Ram, solve_part_1

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
