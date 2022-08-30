from itertools import islice
import sys
from numbers import Number
from typing import List


def solution(seq: List[Number]) -> int:
    sol = [None] * len(seq)
    for i, cur in enumerate(seq):
        sol[i] = 1
        for j, prev in enumerate(islice(seq, i)):
            if cur % prev == 0 and sol[j] + 1 > sol[i]:
                sol[i] = sol[j] + 1
    return max(sol)


if __name__ == '__main__':
    _ = int(next(sys.stdin))
    seq = list(map(int, next(sys.stdin).split()))
    print(solution(seq))
