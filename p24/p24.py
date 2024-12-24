import operator
from typing import Iterable


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

    def get_z(self):
        z_wires = [g for g in self.gates.keys() if g[0] == 'z']
        return sum(2 ** int(wire[1:]) * self.get_value(wire) for wire in z_wires)

    def set_x(self, val: int):
        self.set_input(val, 'x')

    def set_y(self, val: int):
        self.set_input(val, 'y')

    def set_input(self, val: int, xy: str):
        wires = [g for g in self.inits.keys() if g[0] == xy]
        for bit in range(len(wires)):
            self.inits[f"{xy}{bit:02d}"] = bool(val & (2 ** bit))


def solve_part_1(raw_input: str):
    device = Device(raw_input)

    return device.get_z()


def is_and(device: Device) -> bool:
    input_bit_count = sum(1 for x in device.inits.keys() if x[0] == 'x')

    for bit in range(input_bit_count):
        for op1, op2 in (2 ** bit, 2 ** bit), (0, 2 ** bit), (2 ** bit, 0):
            device.set_x(op1)
            device.set_y(op2)

            if device.get_z() != operator.and_(op1, op2):
                return False

    return True


def swapped_device(raw_input: str, gates_to_swap: Iterable[tuple[str, str]]):
    device = Device(raw_input)
    for (a, b) in gates_to_swap:
        swap_gates = {a: device.gates[b],
                      b: device.gates[a]}
        device.gates.update(swap_gates)

    return device
