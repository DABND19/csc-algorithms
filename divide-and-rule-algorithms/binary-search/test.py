import unittest

from main import binary_search


class SolutionTest(unittest.TestCase):
    def test1(self):
        items = [1, 5, 8, 12, 13]
        values_to_search = [8, 1, 23, 1, 11]
        search_results = [2, 0, -1, 0, -1]

        for value, pos in zip(values_to_search, search_results):
            with self.subTest():
                self.assertEqual(binary_search(items, value), pos)

    def test2(self):
        items = []
        self.assertEqual(binary_search(items, 42), -1)

    def test3(self):
        items = [42]
        self.assertEqual(binary_search(items, 42), 0)

    def test4(self):
        items = [42]
        self.assertEqual(binary_search(items, 24), -1)


if __name__ == '__main__':
    unittest.main()
