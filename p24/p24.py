class Device:
    def __init__(self, raw_string: str):
        raw_wires, raw_gates = raw_string.split('\n\n')

        self.inits = dict()
        for wire_line in raw_wires.splitlines():
            s = wire_line.split(': ')
            self.inits.update({s[0]: bool(s[1])})
