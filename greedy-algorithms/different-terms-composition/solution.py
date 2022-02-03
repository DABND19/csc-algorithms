from typing import List


def solution(number: int) -> List[int]:
    composition = []
    term = 1

    while term <= number:
        composition.append(term)
        number -= term
        term += 1

    composition[-1] += number

    return composition


if __name__ == '__main__':
    result = solution(int(input()))
    print(len(result))
    print(*result)
