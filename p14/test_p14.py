from unittest import TestCase

from p14.p14 import Robot, solve_part_1

demo_input_14 = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


class TestRobot(TestCase):
    def test_parse(self):
        raw_input = 'p=0,4 v=3,-3'
        r = Robot(raw_input)
        self.assertEqual((0, 4), r.p_xy)
        self.assertEqual((3, -3), r.v_xy)

    def test_move(self):
        r = Robot('p=2,4 v=2,-3')
        r.move(5, (11, 7))
        self.assertEqual((1, 3), r.p_xy)

    def test_solve_demo_1(self):
        self.assertEqual(12, solve_part_1(demo_input_14, room_size=(11, 7)))

    def test_solve_part_1(self):
        with open('p14/input') as f:
            self.assertEqual(228421332, solve_part_1(f.read()))
