from dataclasses import dataclass
from typing import Mapping, Optional


@dataclass
class Node:
    value: Optional[str] = None
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def __getitem__(self, key: str) -> 'Node':
        if key == '0':
            return self.left
        elif key == '1':
            return self.right
        else:
            raise ValueError('key must be 0 or 1')

    def __setitem__(self, key: str, value: 'Node') -> None:
        if key == '0':
            self.left = value
        elif key == '1':
            self.right = value
        else:
            raise ValueError('key must be 0 or 1')


def build_code_tree(codes: Mapping[str, str]) -> Node:
    head = Node()
    for symbol, code in codes.items():
        current = head
        for digit in code:
            if not current[digit]:
                current[digit] = Node()
            current = current[digit]
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
        current_node = current_node[digit]
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
