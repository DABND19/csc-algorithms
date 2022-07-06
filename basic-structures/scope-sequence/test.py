import unittest
from main import solution


class TestSolution(unittest.TestCase):
    def test_empty_seq(self):
        self.assertEqual(solution(''), None)

    def test_correct_sequence(self):
        self.assertEqual(solution('()[]{}'), None)

    def test_basic_1(self):
        self.assertEqual(solution('{{[()]]'), 6)

    def test_basic_2(self):
        self.assertEqual(solution('()[]}'), 4)

    def test_basic_3(self):
        self.assertEqual(solution('([](){([])})'), None)

    def test_wrong_symbol(self):
        self.assertEqual(solution('{{{**[][][]'), 3)


if __name__ == '__main__':
    unittest.main()
