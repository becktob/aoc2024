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
        operators = {1: self.bxl,
                     2: self.bst,
                     4: self.bxc,
                     5: self.out}
        operator, operand = self.program[self.pointer: self.pointer + 2]

        operators[operator](operand)

    def bxl(self, operand):
        self.B = operand ^ self.B

    def bst(self, operand):
        value = self.combo_operand(operand)
        self.B = value % 8

    def bxc(self, _):
        self.B = self.B ^ self.C

    def out(self, operand):
        self.output.append(self.combo_operand(operand) % 8)

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
