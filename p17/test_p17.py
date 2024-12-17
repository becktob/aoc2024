from unittest import TestCase

from p17.p17 import Computer

demo_input_17 = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""


class TestComputer(TestCase):
    def test_parse(self):
        c = Computer(demo_input_17)
        self.assertEqual(729, c.A)
        self.assertEqual(6, len(c.program))
