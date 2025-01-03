from unittest import TestCase

from p17.p17 import Computer, solve_part_1, simulate, simulate_literal, solve_part_2

demo_input_17 = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

demo_part_2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

with open('p17/input') as f:
    full_part_2 = f.read()


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

    def test_3_adv_jnz(self):
        c = Computer()
        c.A = 2024
        c.program = [0, 1, 5, 4, 3, 0]
        c.run()
        self.assertListEqual([4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0], c.output)
        self.assertEqual(0, c.A)

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

    def test_demo_1(self):
        self.assertEqual("4,6,3,5,6,3,5,2,1,0", solve_part_1(demo_input_17))

    def test_solve_1(self):
        with open('p17/input') as f:
            self.assertEqual('4,1,5,3,1,5,3,5,7', solve_part_1(f.read()))

    def test_program_outputs_self(self):
        c = Computer(demo_part_2)
        c.A = 117440
        c.run()
        self.assertEqual(c.output, c.program)

    def test_demo_2(self):
        self.assertEqual(117440, solve_part_2(demo_part_2))

    def test_solve_2_one_cycle(self):
        c = Computer(full_part_2)
        c.A = 7
        c.run()
        self.assertEqual(0, c.A)
        self.assertEqual([3], c.output)  # Todo: why?

    def test_solve_2_two_cycles(self):
        c = Computer(full_part_2)
        c.A = 5 * 8 * 8 + 7 * 8 + 1
        sim = list(simulate(c.A))
        c.run()
        self.assertEqual(0, c.A)
        self.assertEqual([4, 3, 1], c.output)  # Todo: why?
        self.assertEqual(sim, c.output)

    def test_solve_2_three_cycles(self):
        # output first position is determined by input lsb
        c = Computer(full_part_2)
        c.A = 5 * 8 * 8 * 8 + 7 * 8 * 8 + 1 * 8 + 3
        sim = list(simulate(c.A))
        c.run()
        self.assertEqual(0, c.A)
        self.assertEqual([5, 4, 3, 1], c.output)  # Todo: why?
        self.assertEqual(sim, c.output)

    def test_simulate_refactoring(self):
        A = 3 * 8 * 8 * 8 + 1 * 8 * 8 + 5 * 8 + 7
        literal = list(simulate_literal(A))
        refactored = list(simulate(A))
        self.assertEqual(literal, refactored)

    def test_solve_part_2(self):
        self.assertEqual(164542125272765, solve_part_2(full_part_2))
