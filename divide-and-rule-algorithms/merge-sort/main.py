from collections import deque
from numbers import Number
from typing import List


def merge(seq_1: List[Number], seq_2: List[Number]) -> List[Number]:
    res = []

    it_1 = iter(seq_1)
    it_2 = iter(seq_2)
    val_1 = next(it_1, None)
    val_2 = next(it_2, None)
    for _ in range(len(seq_1) + len(seq_2)):
        if val_1 is None:
            res.append(val_2)
            res.extend(it_2)
            break

        if val_2 is None:
            res.append(val_1)
            res.extend(it_1)
            break

        if val_1 < val_2:
            res.append(val_1)
            val_1 = next(it_1, None)
        else:
            res.append(val_2)
            val_2 = next(it_2, None)

    return res


def merge_sort(
    seq: List[Number]
) -> List[Number]:
    q = deque(map(lambda x: [x], seq))

    while len(q) > 1:
        seq_1 = q.popleft()
        seq_2 = q.popleft()
        q.append(merge(seq_1, seq_2))

    try:
        return q.popleft()
    except IndexError:
        return []
