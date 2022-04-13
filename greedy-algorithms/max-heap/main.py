from numbers import Number
from typing import List


def sift_up(heap: List[Number], pos: int) -> None:
    parent = (pos - 1) // 2
    while pos and heap[pos] > heap[parent]:
        heap[pos], heap[parent] = heap[parent], heap[pos]
        pos = parent
        parent = (pos - 1) // 2


def sift_down(heap: List[Number], pos: int) -> None:
    while True:
        left, right = 2 * pos + 1, 2 * pos + 2
        largest = pos

        if left < len(heap) and heap[largest] < heap[left]:
            largest = left

        if right < len(heap) and heap[largest] < heap[right]:
            largest = right

        if largest == pos:
            break

        heap[pos], heap[largest] = heap[largest], heap[pos]
        pos = largest


def push(heap: List[Number], item: Number) -> None:
    heap.append(item)
    sift_up(heap, len(heap) - 1)


def pop(heap: List[Number]) -> None:
    heap[0], heap[-1] = heap[-1], heap[0]
    res = heap.pop()
    sift_down(heap, 0)
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
