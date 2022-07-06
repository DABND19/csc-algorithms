import sys
from typing import List, Optional, Tuple


def is_bracket(sym: str):
    return sym in {'(', ')', '[', ']', '{', '}'}


def is_opened(bracket: str) -> bool:
    return bracket in {'(', '[', '{'}


def has_same_type(opened_bracket: str, closed_bracket: str) -> bool:
    return (opened_bracket, closed_bracket) in {('(', ')'), ('[', ']'), ('{', '}')}


def solution(bracket_seq: str) -> Optional[int]:
    buf: List[Tuple[int, str]] = []
    for pos, bracket in enumerate(bracket_seq):
        if not is_bracket(bracket):
            continue

        if is_opened(bracket):
            buf.append((pos, bracket))
            continue

        if not buf:
            return pos

        _, pair_bracket = buf.pop()
        if not has_same_type(pair_bracket, bracket):
            return pos

    if not buf:
        return None
    pos, _ = buf[0]
    return pos


if __name__ == '__main__':
    bracket_seq = next(sys.stdin, '').strip()
    res = solution(bracket_seq)
    if res is None:
        print('Success')
    else:
        print(res + 1)
