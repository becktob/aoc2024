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

    def test_1_bst(self):
        c = Computer()
        c.C = 9
        c.program = [2, 6]
        c.one_op()
        self.assertEqual(1, c.B)

    def test_2_out(self):
        c = Computer()
        c.A = 10
        c.program = [5, 0, 5, 1, 5, 4]
        c.run()
        self.assertListEqual([0, 1, 2], c.output)

    def test_4_adv(self):
        c = Computer()
        c.B = 29
        c.program = [1, 7]
        c.one_op()
        self.assertEqual(26, c.B)

    def test_5_bxc(self):
        c = Computer()
        c.B = 2024
        c.C = 43690
        c.program = [4, 0]
        c.one_op()
        self.assertEqual(44354, c.B)
