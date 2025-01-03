from unittest import TestCase

from p02.p02 import report_is_good, solve_part_1, report_is_good_with_dampener, solve_part_2

demo_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


class Test01(TestCase):
    def test_demo_cases_1(self):
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

    def test_demo_cases_2(self):
        demo_reports = (
            ([7, 6, 4, 2, 1], True, ""),
            ([1, 2, 7, 8, 9], False, ""),
            ([9, 7, 6, 2, 1], False, ""),
            ([1, 3, 2, 4, 5], True, ""),
            ([8, 6, 4, 4, 1], True, ""),
        )
        for report, is_good, desc in demo_reports:
            with self.subTest(desc):
                self.assertEqual(is_good, report_is_good_with_dampener(report))

    def test_demo_1(self):
        self.assertEqual(2, solve_part_1(demo_input))

    def test_demo_2(self):
        self.assertEqual(2, solve_part_1(demo_input))

    def test_solve_p02_1(self):
        with open('p02/input') as f:
            self.assertEqual(639, solve_part_1(f.read()))

    def test_solve_p02_2(self):
        with open('p02/input') as f:
            self.assertEqual(674, solve_part_2(f.read()))
