from typing import Any, List


class Node:
    def __init__(self, value: Any = None):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.len: int = 0
        self.head: Node = None
        self.tail: Node = self.head

    def enqueue(self, value):
        new_node = Node(value)
        if not self.tail:
            self.tail = self.head = new_node
        self.len += 1
        self.tail.next = new_node
        self.tail = new_node

    def deque(self):
        if not self.head:
            return None
        self.len -= 1
        head = self.head
        self.head = self.head.next

        return head.value

    def peek(self):
        return self.head.value if self.head else None


new_queue = Queue()


new_queue.enqueue(5)
new_queue.enqueue(7)
new_queue.enqueue(9)

print(new_queue.deque() == 5)
print(new_queue.len == 2)

# // i hate using debuggers
new_queue.enqueue(11)
# debugger;
print(new_queue.deque() == 7)
print(new_queue.deque() == 9)
print(new_queue.peek() == 11)
print(new_queue.deque() == 11)
print(new_queue.deque() is None)
print(new_queue.len == 0)
