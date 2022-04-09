from collections import Counter
import unittest

from main import huffman_encode, build_huffman_codes


class CodesBuilderTest(unittest.TestCase):
    def test1(self):
        freqs = Counter('a')
        codes = {'a': '0'}
        self.assertEqual(build_huffman_codes(freqs), codes)

    def test2(self):
        freqs = Counter('abacabad')
        codes = {'a': '0',
                 'b': '10',
                 'c': '110',
                 'd': '111'}
        self.assertEqual(build_huffman_codes(freqs), codes)

    def test3(self):
        freqs = Counter('beep boop beer!')
        codes = {'b': '00',
                 'e': '11',
                 'p': '101',
                 ' ': '011',
                 'o': '010',
                 'r': '1000',
                 '!': '1001'}
        builded_codes = build_huffman_codes(freqs)

        for symbol, code in builded_codes.items():
            self.assertEqual(len(code), len(codes[symbol]))

            is_unprefixed = all(map(lambda x: not builded_codes[x].startswith(code),
                                    filter(lambda x: x != symbol, builded_codes)))
            self.assertTrue(is_unprefixed)


class EncodingTest(unittest.TestCase):
    def test1(self):
        encoded_str = '0'
        self.assertEqual(huffman_encode('a'), encoded_str)

    def test2(self):
        encoded_str = '01001100100111'
        self.assertEqual(huffman_encode('abacabad'), encoded_str)

    def test3(self):
        encoded_str = '0011111010110001001010101100111110001001'
        decoded_str = 'beep boop beer!'
        self.assertEqual(len(huffman_encode(decoded_str)), len(encoded_str))


if __name__ == '__main__':
    unittest.main()
