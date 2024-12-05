from unittest import TestCase

from p05.p05 import parse_rules_updates, order_is_correct

demo_input_5 = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

class Test(TestCase):

    def test_order_is_correct(self):
        rules, updates = parse_rules_updates(demo_input_5)

        self.assertTrue(order_is_correct(updates[0], rules))
        self.assertTrue(order_is_correct(updates[1], rules))
        self.assertTrue(order_is_correct(updates[2], rules))

        self.assertFalse(order_is_correct(updates[3], rules))
        self.assertFalse(order_is_correct(updates[4], rules))
        self.assertFalse(order_is_correct(updates[5], rules))