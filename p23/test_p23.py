from unittest import TestCase

from p23.p23 import find_direct_triplets, solve_part_1, find_groups, find_largest_direct_group, solve_part_2

demo_input_23 = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


class Test(TestCase):
    def test_find_triplets(self):
        triplets = find_direct_triplets(demo_input_23)
        self.assertEqual(12, len(triplets))

    def test_solve_demo_1(self):
        self.assertEqual(7, solve_part_1(demo_input_23))

    def test_solve_part_1(self):
        with open('p23/input') as f:
            self.assertEqual(1077, solve_part_1(f.read()))

    def test_find_groups(self):
        groups = find_groups(demo_input_23)
        self.assertEqual(1, len(groups))

        with open('p23/input') as f:
            groups = find_groups(f.read())
            self.assertEqual(1, len(groups))

    def test_largest_direct_group(self):
        group = find_largest_direct_group(demo_input_23)
        self.assertEqual(('co', 'de', 'ka', 'ta'), group)

    def test_solve_demo_2(self):
        self.assertEqual('co,de,ka,ta', solve_part_2(demo_input_23))

    def test_solve_part_2(self):
        with open('p23/input') as f:
            self.assertEqual('bc,bf,do,dw,dx,ll,ol,qd,sc,ua,xc,yu,zt', solve_part_2(f.read()))
