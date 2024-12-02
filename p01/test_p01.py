from unittest import TestCase

from p01.p01 import report_is_good

class Test01(TestCase):
    def test_report_is_good_demo(self):
        self.assertTrue(report_is_good([7,6,4,2,1]))
