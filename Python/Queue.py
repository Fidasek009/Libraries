class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None


class Queue:
    """
    A simple queue implementation using LinkedList.

    Attributes:
        first: The first node in the queue.
        last: The last node in the queue.

    Methods:
        enqueue: O(1)
        dequeue: O(1)
        is_empty: O(1)
    """

    def __init__(self) -> None:
        self.first = None
        self.last = None

    def enqueue(self, key):
        new = Node(key)

        if self.is_empty():
            self.first = new
        else:
            self.last.next = new

        self.last = new

    def dequeue(self):
        if self.is_empty():
            return None

        key = self.first.key
        self.first = self.first.next
        return key

    def is_empty(self):
        return self.first is None
