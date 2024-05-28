class Node:
    def __init__(self, key):
        self.key = key
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyLinkedList:
    """
    A simple doubly linked list implementation.

    Attributes:
        first: The first node in the list.
        last: The last node in the list.

    Methods:
        push_back: O(1)
        delete: O(1)
        search: O(n)
        is_empty: O(1)
    """

    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def push_back(self, key) -> Node:
        new = Node(key)
        new.prev = self.tail

        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new

        self.tail = new
        return new

    def delete(self, node: Node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        # release(node)

    def search(self, key) -> Node | None:
        node = self.head

        while node and node.key != key:
            node = node.next

        return node

    def is_empty(self):
        return self.head is None
