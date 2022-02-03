import unittest

from solution import solution


class SolutionTest(unittest.TestCase):
    def test_sample_1(self):
        self.assertEqual(solution(4), [1, 3])


    def test_sample_2(self):
        self.assertEqual(solution(6), [1, 2, 3])


    def test_one(self):
        self.assertEqual(solution(1), [1])


    def test_two(self):
        self.assertEqual(solution(2), [2])


if __name__ == '__main__':
    unittest.main()
