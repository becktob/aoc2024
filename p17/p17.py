import itertools


class Computer:
    def __init__(self, raw_input: str | None = None):
        self.A, self.B, self.C = 0, 0, 0
        self.program: list[int] = []
        self.pointer = 0

        self.output = []

        if raw_input is not None:
            register_lines, program_line = raw_input.split('\n\n')
            self.A, self.B, self.C = map(int, (l.split(':')[1] for l in register_lines.splitlines()))
            self.program = [int(p) for p in program_line.split(':')[1].split(',')]

    def run(self):
        while self.pointer < len(self.program):
            self.one_op()
            self.pointer += 2

    def one_op(self):
        operators = {0: self.adv,
                     1: self.bxl,
                     2: self.bst,
                     3: self.jnz,
                     4: self.bxc,
                     5: self.out,
                     6: self.bdv,
                     7: self.cdv}
        operator, operand = self.program[self.pointer: self.pointer + 2]

        operators[operator](operand)

    def adv(self, operand):
        denominator = 2 ** self.combo_operand(operand)
        self.A = self.A // denominator

    def bxl(self, operand):
        self.B = operand ^ self.B

    def jnz(self, operand):
        if self.A == 0:
            return
        else:
            self.pointer = operand - 2  # pointer is +=2 in run()

    def bst(self, operand):
        value = self.combo_operand(operand)
        self.B = value % 8

    def bxc(self, _):
        self.B = self.B ^ self.C

    def out(self, operand):
        self.output.append(self.combo_operand(operand) % 8)

    def bdv(self, operand):
        denominator = 2 ** self.combo_operand(operand)
        self.B = self.A // denominator

    def cdv(self, operand):
        denominator = 2 ** self.combo_operand(operand)
        self.C = self.A // denominator

    def combo_operand(self, operand):
        if operand < 4:
            return operand
        elif operand == 4:
            return self.A
        elif operand == 5:
            return self.B
        elif operand == 6:
            return self.C
        elif operand == 7:
            raise ValueError("Combo operand 7 is reserved and will not appear in valid programs.")


def solve_part_1(raw_input):
    c = Computer(raw_input)
    c.run()
    return ','.join(map(str, c.output))


def solve_part_2(raw_input):
    for i in itertools.count():
        c = Computer(raw_input)
        c.A = i
        c.run()
        if c.output == c.program:
            return i


def simulate_literal(A):
    # translate input program:
    while A != 0:  # jnz at end of program
        B = A % 8
        B = B ^ 1
        C = A // 2 ** B
        B = B ^ 5
        A = A // 8
        B = B ^ C
        yield B % 8  # out


def convert_one_byte(A_byte):
    B = A_byte
    B = B ^ 1
    C = A_byte // 2 ** B
    B = B ^ 5
    B = B ^ C
    return B % 8


def simulate(A):
    while A != 0:
        yield convert_one_byte(A % 8)
        A = A // 8
