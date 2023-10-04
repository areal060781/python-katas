import unittest
from hackerrank.bigger_is_greater import bigger_is_greater2 as big


class TestBiggerIsGreater(unittest.TestCase):

    def test_default_cases(self):
        self.assertEqual(big('abcd'), 'abdc')
        self.assertEqual(big('ab'), 'ba')
        self.assertEqual(big('hefg'), 'hegf')
        self.assertEqual(big('dhck'), 'dhkc')
        self.assertEqual(big('dkhc'), 'hcdk')
        self.assertEqual(big('lmno'), 'lmon')
        self.assertEqual(big('abdc'), 'acbd')
        self.assertEqual(big('dcba'), 'no answer')
        self.assertEqual(big('dcbb'), 'no answer')
        self.assertEqual(big('bb'), 'no answer')

    def test_extra_cases(self):
        self.assertEqual(big('zzzayybbaa'), 'zzzbaaabyy')
        # self.assertEqual(big('gkbekyrhcwc'), 'gkbekyrhwcc')
        # self.assertEqual(big('sajpyegttujxyx'), 'sajpyegttujyxx')
        # self.assertEqual(big('yitveovrja'), 'yitverajov')
        # self.assertEqual(big('xildrrhpca'), 'xildrrpach')


if __name__ == '__main__':
    unittest.main()
