from unittest import TestCase

from p01.p01 import report_is_good, solve_p01


class Test01(TestCase):
    def test_steps_small_enough(self):
        demo_reports = (
            ([7, 6, 4, 2, 1], True),
            ([1, 2, 7, 8, 9], False),
            ([9, 7, 6, 2, 1], False),
        )
        for report, is_good in demo_reports:
            with self.subTest(report):
                self.assertEqual(is_good, report_is_good(report))

    def test_steps_same_sign(self):
        demo_reports = (
            ([1, 3, 2, 4, 5], False),
        )
        for report, is_good in demo_reports:
            with self.subTest(report):
                self.assertEqual(is_good, report_is_good(report))

    def test_steps_not_zero(self):
        demo_reports = (
            ([8, 6, 4, 4, 1], False),
        )
        for report, is_good in demo_reports:
            with self.subTest(report):
                self.assertEqual(is_good, report_is_good(report))

    def test_demo(self):
        demo_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
        self.assertEqual(2, solve_p01(demo_input))
