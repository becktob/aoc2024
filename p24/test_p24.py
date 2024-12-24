from unittest import TestCase

from p24.p24 import Device, solve_part_1

demo_24_small = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
"""


class TestDevice(TestCase):
    def test_parse(self):
        device = Device(demo_24_small)
        self.assertEqual(False, device.inits['y02'])

        gate = device.gates['z00']
        self.assertEqual(('x00', 'y00'), gate.inputs)

    def test_get_value(self):
        device = Device(demo_24_small)

        self.assertEqual(False, device.get_value('z00'))
        self.assertEqual(False, device.get_value('z01')),
        self.assertEqual(True, device.get_value('z02'))

    def test_solve_demo_1_small(self):
        self.assertEqual(4, solve_part_1(demo_24_small))
