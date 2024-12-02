from unittest import TestCase

from p01.p01 import report_is_good


class Test01(TestCase):
    def test_report_is_good_demo(self):
        demo_reports = (
            ([7, 6, 4, 2, 1], True),
            ([1, 2, 7, 8, 9], False),
            ([9, 7, 6, 2, 1], False),
        )
        for report, is_good in demo_reports:
            with self.subTest(report):
                self.assertEqual(is_good, report_is_good(report))
