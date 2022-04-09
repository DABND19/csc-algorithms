from dataclasses import dataclass
from typing import Mapping, Optional


@dataclass
class Node:
    value: Optional[str] = None
    left: Optional['Node'] = None
    right: Optional['Node'] = None


def build_code_tree(codes: Mapping[str, str]) -> Node:
    head = Node()
    for symbol, code in codes.items():
        current = head
        for digit in code:
            if digit == '0':
                if not current.left:
                    current.left = Node()
                current = current.left
            elif digit == '1':
                if not current.right:
                    current.right = Node()
                current = current.right
            else:
                raise ValueError(f'Wrong Huffman code: {code}')
        current.value = symbol
    return head


def solution(
    codes: Mapping[str, str],
    encoded_str: str
) -> str:
    decoded_str = ''

    head_node = build_code_tree(codes)
    current_node = head_node
    for digit in encoded_str:
        if digit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.value is not None:
            decoded_str += current_node.value
            current_node = head_node

    return decoded_str


if __name__ == '__main__':
    codes_count, encoded_str_len = map(int, input().split())

    codes = {}
    for _ in range(codes_count):
        symbol, _, code = input().partition(': ')
        codes[symbol] = code

    encoded_str = input()

    print(solution(codes, encoded_str))
