from numbers import Number
from typing import List, Tuple


def get_parent_index(index: int) -> int:
    if index == 0:
        return 0
    return (index - 1) // 2


def get_children_indicies(index: int) -> Tuple[int, int]:
    return 2 * index + 1, 2 * index + 2


def push(heap: List[Number], item: Number) -> None:
    i = len(heap)
    heap.append(item)
    while heap[i] > heap[get_parent_index(i)]:
        heap[i], heap[get_parent_index(i)] = heap[get_parent_index(i)], heap[i]
        i = get_parent_index(i)


def pop(heap: List[Number]) -> None:
    heap[0], heap[-1] = heap[-1], heap[0]
    res = heap.pop()

    i = 0
    while True:
        left, right = get_children_indicies(i)
        largest = i

        if left < len(heap) and heap[largest] < heap[left]:
            largest = left

        if right < len(heap) and heap[largest] < heap[right]:
            largest = right

        if largest == i:
            break

        heap[i], heap[largest] = heap[largest], heap[i]
        i = largest

    return res


if __name__ == '__main__':
    instructions_count = int(input())

    heap = []
    actions = {'Insert': push,
               'ExtractMax': pop}
    for _ in range(instructions_count):
        instruction, *args = input().split()
        res = actions[instruction](heap, *map(int, args))
        if res is not None:
            print(res)
