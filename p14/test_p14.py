from unittest import TestCase

from p14.p14 import Robot


class TestRobot(TestCase):
    def test_parse(self):
        raw_input = 'p=0,4 v=3,-3'
        r = Robot(raw_input)
        self.assertEqual((0, 4), r.p_xy)
        self.assertEqual((3, -3), r.v_xy)

    def test_move(self):
        r = Robot('p=2,4 v=2,-3')
        r.move(5, (11,7))
        self.assertEqual((1,3),r.p_xy)
