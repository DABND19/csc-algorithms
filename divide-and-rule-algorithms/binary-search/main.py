from numbers import Number
from typing import List


def binary_search(items: List[Number], value: Number) -> int:
    begin = 0
    end = len(items)

    while end - begin > 1:
        middle = begin + (end - begin) // 2

        if value < items[middle]:
            end = middle
        else:
            begin = middle

    if len(items) and items[begin] == value:
        return begin
    else:
        return -1


if __name__ == '__main__':
    _, *items = map(int, input().split())
    _, *queries = map(int, input().split())

    search_results = []
    for query in queries:
        pos = binary_search(items, query)
        if pos != -1:
            pos += 1
        search_results.append(pos)

    print(*search_results)
