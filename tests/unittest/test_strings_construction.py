import unittest
from katas import strings_construction


class TestStringsConstruction(unittest.TestCase):
    def test_construction(self):
        self.assertEqual(strings_construction('abc', 'abccba'), 2)
        self.assertEqual(strings_construction('ab', 'abcbcb'), 1)
        self.assertEqual(strings_construction('ar', 'margarita'), 2)


if __name__ == '__main__':
    unittest.main()
