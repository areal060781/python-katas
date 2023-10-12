import unittest
from katas import time_in_words


class TestTimeInWords(unittest.TestCase):
    def test_time_in_words(self):
        self.assertEqual(time_in_words(5, 30), 'half past five')
        self.assertEqual(time_in_words(3, 30), 'half past three')
        self.assertEqual(time_in_words(5, 00), "five o' clock")
        self.assertEqual(time_in_words(5, 15), 'quarter past five')
        self.assertEqual(time_in_words(5, 45), 'quarter to six')
        self.assertEqual(time_in_words(6, 1), 'one minute past six')
        self.assertEqual(time_in_words(6, 47), 'thirteen minutes to seven')


if __name__ == '__main__':
    unittest.main()
