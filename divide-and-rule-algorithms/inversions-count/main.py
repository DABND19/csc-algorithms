from numbers import Number
import sys
from typing import List, Tuple


def merge_and_count_inversions(
    seq_left: List[Number], 
    seq_right: List[Number]
) -> Tuple[List[Number], int]:
    idx_left = 0
    idx_right = 0

    inversions_count = 0
    merged_seq = []
    while len(merged_seq) != len(seq_left) + len(seq_right):
        try:
            left = seq_left[idx_left]
        except IndexError:
            merged_seq.extend(seq_right[idx_right:])
            continue

        try:
            right = seq_right[idx_right]
        except IndexError:
            merged_seq.extend(seq_left[idx_left:])
            continue

        if left <= right:
            merged_seq.append(left)
            idx_left += 1
        else:
            merged_seq.append(right)
            inversions_count += (len(seq_left) - idx_left)
            idx_right += 1
    return merged_seq, inversions_count


def solution(seq: List[Number]) -> Tuple[List[Number], int]:
    if len(seq) <= 1:
        return seq, 0

    left = seq[:len(seq) // 2]
    right = seq[len(seq) // 2:]
    left, inv_left = solution(left)
    right, inv_right = solution(right)
    merged, inv = merge_and_count_inversions(left, right)
    inv += inv_left + inv_right
    return merged, inv


if __name__ == '__main__':
    _ = next(sys.stdin, 0)
    seq = list(map(int, next(sys.stdin, '').split()))
    _, inv = solution(seq)
    print(inv)
