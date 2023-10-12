import unittest
from katas.kaprekar_numbers import kaprekar_numbers


class TestKaprekarNumbers(unittest.TestCase):
    def test_case_6(self):
        self.assertEqual(kaprekar_numbers(1, 99999),
                         '1 9 45 55 99 297 703 999 2223 2728 4950 5050 7272 7777 9999 17344 22222 77778 82656 95121 99999')

    def test_case_0(self):
        self.assertEqual(kaprekar_numbers(1, 100), '1 9 45 55 99')

    def test_case_1(self):
        self.assertEqual(kaprekar_numbers(100, 300), '297')


if __name__ == '__main__':
    unittest.main()
