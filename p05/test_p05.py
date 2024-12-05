from unittest import TestCase

from p05.p05 import parse_rules_updates, solve_part_1, Update, solve_part_2

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

        self.assertTrue(updates[0].is_ordered(rules))
        self.assertTrue(updates[1].is_ordered(rules))
        self.assertTrue(updates[2].is_ordered(rules))

        self.assertFalse(updates[3].is_ordered(rules))
        self.assertFalse(updates[4].is_ordered(rules))
        self.assertFalse(updates[5].is_ordered(rules))

    def test_solve_demo_1(self):
        self.assertEqual(143, solve_part_1(demo_input_5))

    def test_solve_part_1(self):
        with open('p05/input') as f:
            self.assertEqual(5452, solve_part_1(f.read()))

    def test_ordering(self):
        rules, updates = parse_rules_updates(demo_input_5)
        update = Update('75,97,47,61,53')
        update.order(rules)
        self.assertEqual([97, 75, 47, 61, 53], update.pages)

    def test_solve_demo_2(self):
        self.assertEqual(123, solve_part_2(demo_input_5))

    def test_solve_part_2(self):
        with open('p05/input') as f:
            self.assertEqual(0, solve_part_2(f.read()))
