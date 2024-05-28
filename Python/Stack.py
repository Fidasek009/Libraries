class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.below: Node | None = None


class Stack:
    """
    A simple stack implementation using LinkedList.

    Attributes:
        top: The top node in the stack.

    Methods:
        push: O(1)
        pop: O(1)
        is_empty: O(1)
    """

    def __init__(self) -> None:
        self.top: Node | None = None

    def pop(self):
        if self.is_empty():
            return None

        key = self.top.key
        self.top = self.top.below

        return key

    def push(self, key):
        new = Node(key)
        new.below = self.top
        self.top = new

    def is_empty(self):
        return self.top is None
