from unittest import TestCase

from p14.p14 import Robot


class TestRobot(TestCase):
    def test_parse(self):
        raw_input = 'p=0,4 v=3,-3'
        r = Robot(raw_input)
        self.assertEqual((0, 4), r.p_xy)
        self.assertEqual((3, -3), r.v_xy)
