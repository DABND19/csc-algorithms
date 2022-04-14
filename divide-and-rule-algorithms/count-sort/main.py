from itertools import chain, repeat
from typing import List


def count_sort(
    seq: List[int],
    max_value: int
) -> List[int]:
    counter = [0 for _ in range(max_value + 1)]
    for val in seq:
        counter[val] += 1
    repeats = (repeat(item, count)
               for item, count in enumerate(counter))
    return list(chain.from_iterable(repeats))


if __name__ == '__main__':
    items_count = int(input())
    items = list(map(int, input().split()))
    sorted_items = count_sort(items, max_value=10)
    print(*sorted_items)
