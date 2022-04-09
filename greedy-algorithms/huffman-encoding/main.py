from collections import Counter
import heapq
from typing import Mapping


def build_huffman_codes(freqs: Mapping[str, int]):
    if len(freqs) == 1:
        return {symbol: '0' for symbol in freqs}

    queue = [(freq, symbol) for symbol, freq in freqs.items()]
    heapq.heapify(queue)

    codes = {symbol: '' for symbol in freqs}
    while len(queue) > 1:
        freq_1, symbols_1 = heapq.heappop(queue)
        freq_2, symbols_2 = heapq.heappop(queue)

        for symbol in symbols_1:
            codes[symbol] = '0' + codes[symbol]

        for symbol in symbols_2:
            codes[symbol] = '1' + codes[symbol]

        heapq.heappush(queue,
                       (freq_1 + freq_2,
                        symbols_1 + symbols_2))

    return codes


def huffman_encode(string: str) -> str:
    freqs = Counter(string)
    huffman_codes = build_huffman_codes(freqs)
    huffman_table = str.maketrans(huffman_codes)
    return string.translate(huffman_table)


if __name__ == '__main__':
    string = input()

    freqs = Counter(string)
    huffman_codes = build_huffman_codes(freqs)
    huffman_table = str.maketrans(huffman_codes)
    encoded_str = string.translate(huffman_table)

    print(len(freqs), len(encoded_str))
    for symbol, code in huffman_codes.items():
        print(f'{symbol}: {code}')
    print(encoded_str)
