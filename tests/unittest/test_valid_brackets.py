import unittest
from katas.valid_brackets import valid_bracket_sequence


class TestValidBrackets(unittest.TestCase):
    def test_valid_sequence(self):
        self.assertTrue(valid_bracket_sequence('{{}}()[()]'))
        self.assertFalse(valid_bracket_sequence('{][}'))
        self.assertFalse(valid_bracket_sequence(')'))
        self.assertTrue(valid_bracket_sequence('()'))
        self.assertTrue(valid_bracket_sequence('()[]{}'))
        self.assertFalse(valid_bracket_sequence('(]'))
        self.assertFalse(valid_bracket_sequence('([)]'))
        self.assertTrue(valid_bracket_sequence('{[]}'))


if __name__ == '__main__':
    unittest.main()
