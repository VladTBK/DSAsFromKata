from typing import Any, Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional[Node] = None


class Stack:
    def __init__(self) -> None:
        self.len = 0
        self.head: Optional[Node] = None

    def push(self, value: int) -> None:
        new_node = Node(value)
        self.len += 1
        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def pop(self) -> int | None:
        if not self.head:
            return None

        self.len -= 1
        curr_val = self.head.value
        self.head = self.head.next
        return curr_val

    def peek(self) -> int | None:
        return self.head.value if self.head else None


new_stack = Stack()
new_stack.push(5)
new_stack.push(7)
new_stack.push(9)

print(new_stack.pop() == 9)
print(new_stack.len == 2)

new_stack.push(11)
print(new_stack.pop() == 11)
print(new_stack.pop() == 7)
print(new_stack.peek() == 5)
print(new_stack.pop() == 5)
print(new_stack.pop() is None)
