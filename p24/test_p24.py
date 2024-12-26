import operator
from unittest import TestCase, skip

from p24.p24 import Device, solve_part_1, swapped_device, solve_part_2, is_operator

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

with open('p24/input') as f:
    full_input_24 = f.read()


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
        self.assertFalse(is_operator(device, operator.and_))

    def test_is_and_repaired(self):
        repaired_device = swapped_device(demo_24_add, (('z00', 'z05'), ('z02', 'z01')))
        self.assertTrue(is_operator(repaired_device, operator.and_))

    def test_solve_demo_2(self):
        self.assertEqual('z00,z01,z02,z05', solve_part_2(demo_24_add, operator.and_, 2))

    @skip('slow')
    def test_solve_part_2_brute(self):
        self.assertEqual(1, full_input_24)

    def test_unmodified_device(self):
        device = Device(full_input_24)
        self.assertFalse(is_operator(device, operator.add))

    def test_solve_part_2(self):
        swaps = [('kfp', 'hbs'),  # <kfp = 'x09' AND 'y09'> => <hbs = 'y09' XOR 'x09'>
                 ('z18', 'dhq'),  # <z18 = 'x18' AND 'y18'> => <dhq = <fwt = 'y18' XOR 'x18'> XOR <pvk ...
                 ('z22', 'pdg'),  # <z22 = <bqp = 'x22' AND 'y22'> ... => <pdg = <dbp = 'x22' XOR 'y22'> ...
                 ('z27', 'jcp'),  # <z27 = <ckj> AND <bch> => "<jcp = <ckj> XOR <bch>'"
                 ]

        device = swapped_device(full_input_24, swaps)
        self.assertTrue(is_operator(device, operator.add))

        sorted_involved = sorted(g for swap in swaps for g in swap)
        self.assertEqual('dhq,hbs,jcp,kfp,pdg,z18,z22,z27', ','.join(sorted_involved))
