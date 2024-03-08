from trees import tree1, left, right, value
from typing import Any, List

node = tree1


### DFS
def walk_pre(node: Any, path: list[int]) -> None:
    if not node:
        return
    path.append(node[value])
    walk_pre(node[left], path)
    walk_pre(node[right], path)


def walk_in(node: Any) -> None:
    if not node:
        return
    walk_in(node[left])
    print(node[value])
    walk_in(node[right])


def walk_post(node: Any) -> None:
    if not node:
        return
    walk_post(node[left])
    walk_post(node[right])
    print(node[value])


### BFS

print(node)
path: list[int] = []
walk_pre(tree1, path)
print(path)
