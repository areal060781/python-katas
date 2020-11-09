import unittest
from hackerrank.meal_cost import solve


class TestMealCost(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(12.0, 20, 8), 15)
        self.assertEqual(solve(15.50, 15, 10), 19)
        self.assertEqual(solve(10.25, 17, 5), 13)

if __name__ == '__main__':
    unittest.main()