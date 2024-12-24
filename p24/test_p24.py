from unittest import TestCase

from p24.p24 import Device, solve_part_1, swapped_device, is_and

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

demo_24_add = """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
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

    def test_solve_part_1(self):
        with open('p24/input') as f:
            self.assertEqual(69201640933606, solve_part_1(f.read()))

    def test_is_and(self):
        device = swapped_device(demo_24_add, ())
        self.assertFalse(is_and(device))

    def test_is_and_repaired(self):
        repaired_device = swapped_device(demo_24_add, (('z00', 'z05'), ('z02', 'z01')))
        self.assertTrue(is_and(repaired_device))
