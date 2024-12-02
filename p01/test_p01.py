from unittest import TestCase

from p01.p01 import report_is_good, solve_p01


class Test01(TestCase):
    def test_demo_1(self):
        demo_reports = (
            ([7, 6, 4, 2, 1], True, "ok"),
            ([1, 2, 7, 8, 9], False, "inc 5"),
            ([9, 7, 6, 2, 1], False, "inc 4"),
            ([1, 3, 2, 4, 5], False, "Mix increasing/decreasing"),
            ([8, 6, 4, 4, 1], False, "no change"),
        )
        for report, is_good, desc in demo_reports:
            with self.subTest(desc):
                self.assertEqual(is_good, report_is_good(report))

    def test_parse_demo(self):
        demo_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
        self.assertEqual(2, solve_p01(demo_input))

    def test_solve_p01(self):
        with open('p01/input') as f:
            self.assertEqual(639, solve_p01(f.read()))
