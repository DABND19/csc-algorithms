import unittest

from main import solution


class SolutionTest(unittest.TestCase):
    def test1(self):
        codes = {'a': '0'}
        self.assertEqual(solution(codes, '0'), 'a')

    def test2(self):
        codes = {'a': '0',
                 'b': '10',
                 'c': '110',
                 'd': '111'}
        encoded_str = '01001100100111'
        decoded_str = 'abacabad'
        self.assertEqual(solution(codes, encoded_str),
                         decoded_str)

    def test3(self):
        codes = {'b': '00',
                 'e': '11',
                 'p': '101',
                 ' ': '011',
                 'o': '010',
                 'r': '1000',
                 '!': '1001'}
        encoded_str = '0011111010110001001010101100111110001001'
        decoded_str = 'beep boop beer!'
        self.assertEqual(solution(codes, encoded_str),
                         decoded_str)


if __name__ == '__main__':
    unittest.main()
