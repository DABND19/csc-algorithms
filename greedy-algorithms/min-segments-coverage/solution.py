from typing import List, Optional, Tuple, NewType


Point = NewType('Point', float)
Segment = NewType('Segment', Tuple[Point, Point])


def intersect_segments(segment_1: Segment, segment_2: Segment) -> Optional[Segment]:
    left_1, right_1 = segment_1
    left_2, right_2 = segment_2

    if right_1 < left_2 or right_2 < left_1:
        return None

    return (max(left_1, left_2), min(right_1, right_2))


def solution(segments: List[Segment]) -> List[Point]:
    intersections = []

    for segment in sorted(segments):
        if intersections and intersect_segments(intersections[-1], segment):
            intersections[-1] = intersect_segments(intersections[-1], segment)
        else:
            intersections.append(segment)

    return [right for _, right in intersections]


if __name__ == '__main__':
    segments_count = int(input())
    segments = [tuple(map(Point, input().split())) 
                for _ in range(segments_count)]

    result = solution(segments)

    print(len(result))
    print(*result)
