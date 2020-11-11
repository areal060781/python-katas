import unittest
from hackerrank.bigger_is_greater import bigger_is_greater as big


class TestBiggerIsGreater(unittest.TestCase):
    def test_lexicographical_order(self):
        self.assertEqual(big('abcd'), 'abdc')
        self.assertEqual(big('ab'), 'ba')
        self.assertEqual(big('bb'), 'no answer')
        self.assertEqual(big('hefg'), 'hegf')
        self.assertEqual(big('dhck'), 'dhkc')
        self.assertEqual(big('dkhc'), 'hcdk')
        self.assertEqual(big('lmno'), 'lmon')
        self.assertEqual(big('dcba'), 'no answer')
        self.assertEqual(big('dcbb'), 'no answer')
        self.assertEqual(big('abdc'), 'acbd')


if __name__ == '__main__':
    unittest.main()
