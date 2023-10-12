import unittest
from katas.right_justify import right_justify


class TestJustify(unittest.TestCase):
    def test_right_justify(self):
        self.assertEqual(len(right_justify('Aida')), 70)


if __name__ == '__main__':
    unittest.main()

