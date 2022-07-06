from dataclasses import dataclass
from itertools import chain
import sys
from typing import List, Optional


@dataclass
class Node:
    id: int
    parent: Optional['Node']
    children: List['Node']

    @classmethod
    def from_parent_ids(cls, parent_ids: List[int]) -> 'Node':
        nodes = [Node(node_id, None, [])
                 for node_id in range(len(parent_ids))]
        for node_id, parent_id in enumerate(parent_ids):
            node = nodes[node_id]
            if parent_id == -1:
                continue
            parent = nodes[parent_id]
            node.parent = parent
            parent.children.append(node)
        [root] = filter(lambda n: n.parent is None, nodes)
        return root


def solution(tree: Node) -> int:
    to_walk = tree.children
    depth = 1
    while to_walk:
        depth += 1
        to_walk = list(chain.from_iterable(node.children for node in to_walk))
    return depth


if __name__ == '__main__':
    _ = next(sys.stdin, '')
    nodes = list(map(int, next(sys.stdin, '').split()))
    tree = Node.from_parent_ids(nodes)
    print(solution(tree))
