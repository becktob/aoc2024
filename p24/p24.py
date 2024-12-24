import operator


class Gate:
    def __init__(self, raw_line: str):
        raw_inputs, self.result_wire = raw_line.split(' -> ')
        in_1, op, in_2 = raw_inputs.split()

        self.inputs = (in_1, in_2)
        self.op = {'AND': operator.and_,
                   'OR': operator.or_,
                   'XOR': operator.xor}[op]


class Device:
    def __init__(self, raw_string: str):
        raw_wires, raw_gates = raw_string.split('\n\n')

        self.inits = dict()
        for wire_line in raw_wires.splitlines():
            s = wire_line.split(': ')
            self.inits.update({s[0]: bool(s[1])})

        self.gates = dict()
        for line in raw_gates.splitlines():
            gate = Gate(line)
            self.gates.update({gate.result_wire: gate})
