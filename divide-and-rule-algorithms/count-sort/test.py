import random
import unittest

from main import count_sort


class CountSortTest(unittest.TestCase):
    def test_random(self):
        max_value = 10
        seq = random.choices(list(range(max_value + 1)),
                             k=random.randint(1, 10**4))
        sorted_seq = count_sort(seq, max_value)
        is_sorted = all(first <= second for first, second
                        in zip(sorted_seq, sorted_seq[1:]))
        self.assertTrue(is_sorted)


if __name__ == '__main__':
    unittest.main()
