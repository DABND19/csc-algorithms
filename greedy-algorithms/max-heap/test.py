from numbers import Number
import random
from typing import List
import unittest

from main import push, pop, get_children_indicies


def is_max_heap(heap: List[Number]) -> bool:
    res = True
    for current, value in enumerate(heap):
        left, right = get_children_indicies(current)

        if left < len(heap):
            res = res and value >= heap[left]

        if right < len(heap):
            res = res and value >= heap[right]
    return res


class PushTest(unittest.TestCase):
    def test1(self):
        limit = random.randint(0, 10**5)
        heap = []

        for num in range(limit + 1):
            push(heap, num)

        self.assertEqual(heap[0], limit)
        self.assertTrue(is_max_heap(heap))


class PopTest(unittest.TestCase):
    def test1(self):
        limit = random.randint(0, 10**5)
        heap = list(reversed(range(limit + 1)))

        self.assertEqual(pop(heap), limit)
        self.assertTrue(is_max_heap(heap))

        sorted_array = [limit]
        while heap:
            sorted_array.append(pop(heap))

        self.assertEqual(sorted_array, 
                         list(reversed(range(limit + 1))))


class SolutionTest(unittest.TestCase):
    def test1(self):
        heap = []
        push(heap, 200)
        push(heap, 10)
        self.assertEqual(pop(heap), 200)
        push(heap, 5)
        push(heap, 500)
        self.assertEqual(pop(heap), 500)


if __name__ == '__main__':
    unittest.main()
