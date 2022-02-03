from typing import NamedTuple, List


class Item(NamedTuple):
    cost: float
    weight: float


    @property
    def price(self):
        return self.cost / self.weight


def solution(
    items: List[Item], 
    max_capacity: float
) -> float:
    capacity = max_capacity
    total_cost = 0

    for item in sorted(items, key=lambda x: x.price, reverse=True):
        possible_weight = item.weight if item.weight <= capacity else capacity
        total_cost += item.price * possible_weight
        capacity -= possible_weight

    return total_cost


if __name__ == '__main__':
    items_count, max_capacity = input().split()
    items_count = int(items_count)
    max_capacity = float(max_capacity)

    items = [Item(*map(float, input().split())) 
             for _ in range(items_count)]

    max_cost = solution(items, max_capacity)
    print(f'{max_cost:.3f}')
