import unittest
from katas import cut_the_sticks


class TestCutTheSticks(unittest.TestCase):
    def test_cutting(self):
        self.assertListEqual(cut_the_sticks([8, 8, 14, 10, 3, 5, 14, 12]), [8, 7, 6, 4, 3, 2])

if __name__ == '__main__':
    unittest.main()
