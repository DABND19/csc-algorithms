import unittest

from main import solution


class TestSolution(unittest.TestCase):
    def test_basic(self):
        seq = [2, 3, 9, 2, 9]
        _, inv = solution(seq)
        self.assertEqual(inv, 2)


if __name__ == '__main__':
    unittest.main()
