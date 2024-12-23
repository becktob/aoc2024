from tokenize import group
from unittest import TestCase

from p23.p23 import find_direct_triplets

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
    def test_find_gropus(self):
        groups = find_direct_triplets(demo_input_23)
        self.assertEqual(12, len(groups))
