class Computer:
    def __init__(self, raw_input: str | None):
        self.A, self.B, self.C = 0, 0, 0
        self.program: list[int] = []

        if raw_input is not None:
            register_lines, program_line = raw_input.split('\n\n')
            self.A, self.B, self.C = map(int, (l.split(':')[1] for l in register_lines.splitlines()))
            self.program = [int(p) for p in program_line.split(':')[1].split(',')]
