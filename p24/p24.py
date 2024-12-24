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
            self.inits.update({s[0]: (True if s[1] == '1' else False)})

        self.gates = dict()
        for line in raw_gates.splitlines():
            gate = Gate(line)
            self.gates.update({gate.result_wire: gate})

    def get_value(self, wire):
        if wire in self.inits:
            return self.inits[wire]

        gate = self.gates[wire]
        input_values = [self.get_value(i) for i in gate.inputs]
        return gate.op(*input_values)
