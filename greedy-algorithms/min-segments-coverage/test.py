import unittest

from solution import solution, intersect_segments


class SegmentsIntersectionTest(unittest.TestCase):
    def test_inner(self):
        self.assertEqual(intersect_segments((1, 4), (2, 3)), (2, 3))


    def test_edge(self):
        self.assertEqual(intersect_segments((1, 3), (2, 3)), (2, 3))


    def test_empty(self):
        self.assertEqual(intersect_segments((1, 2), (3, 4)), None)


    def test_point(self):
        self.assertEqual(intersect_segments((1, 2), (2, 3)), (2, 2))


class SolutionTest(unittest.TestCase):
    def test_simple_1(self):
        result = solution([
            (1, 3), 
            (2, 5), 
            (3, 6),
        ])
        self.assertEqual(len(result), 1)


    def test_simple_2(self):
        result = solution([
            (4, 7),
            (1, 3),
            (2, 5),
            (5, 6),
        ])
        self.assertEqual(len(result), 2)


    def test_empty(self):
        self.assertEqual(solution([]), [])


    def test_single(self):
        result = solution([(1, 2)])
        self.assertEqual(len(result), 1)


    def test_empty_intersection(self):
        result = solution([
            (1, 2), 
            (3, 4), 
            (5, 6), 
            (7, 8)
        ])
        self.assertEqual(len(result), 4)


if __name__ == '__main__':
    unittest.main()
