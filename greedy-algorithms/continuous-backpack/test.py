import unittest

from solution import solution, Item


class SolutionTest(unittest.TestCase):
    def test_sample(self):
        items = [
            Item(60, 20), 
            Item(100, 50), 
            Item(120, 30)
        ]
        max_capacity = 50
        self.assertEqual(solution(items, max_capacity), 180)


    def test_empty(self):
        self.assertEqual(solution([], 1000), 0)


    def test_zero_capacity(self):
        items = [
            Item(60, 20), 
            Item(100, 50), 
            Item(120, 30)
        ]
        self.assertEqual(solution(items, 0), 0)


if __name__ == '__main__':
    unittest.main()
