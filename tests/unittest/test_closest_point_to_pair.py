import unittest

from hackerrank.closest_point_to_pair import closest_point_pair


class TestClosestPointToPair(unittest.TestCase):
    def test_points(self):
        self.assertEqual(closest_point_pair([[0, 11], [-7, 1], [-5, -3]]), 4.47213595499958)


if __name__ == '__main__':
    unittest.main()
