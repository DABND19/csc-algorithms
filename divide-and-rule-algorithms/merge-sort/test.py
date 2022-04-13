import unittest
import random

from main import merge, merge_sort


class MergeTest(unittest.TestCase):
    def test1(self):
        seq_1 = list(range(0, 1000, 2))
        seq_2 = list(range(1, 1000, 2))
        merged = list(range(1000))
        self.assertEqual(merge(seq_1, seq_2), merged)

    def test2(self):
        seq_1 = []
        seq_2 = list(range(1000))
        self.assertEqual(merge(seq_1, seq_2), seq_2)

    def test3(self):
        seq_1 = list(range(500))
        seq_2 = list(range(500, 1000))
        merged = list(range(1000))
        self.assertEqual(merge(seq_1, seq_2), merged)

    def test4(self):
        self.assertEqual(merge([], []), [])


class MergeSortTest(unittest.TestCase):
    def test1(self):
        seq = list(reversed(range(1000)))
        sorted_seq = list(range(1000))
        self.assertEqual(merge_sort(seq), sorted_seq)

    def test2(self):
        seq = []
        self.assertEqual(merge_sort(seq), seq)

    def test3(self):
        seq = list(range(1000))
        random.shuffle(seq)
        sorted_seq = list(range(1000))
        self.assertEqual(merge_sort(seq), sorted_seq)


if __name__ == '__main__':
    unittest.main()
