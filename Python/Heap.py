def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def cmp_min(x, y):
    return x < y


def cmp_max(x, y):
    return x > y


class Heap:
    """
    Binary heap implementation.

    Attributes:
        data: list of elements
        cmp: comparison function

    Methods:
        build_heap: O(n)
        heapify: O(log n)
        top: O(1)
        extract_top: O(log n)
        insert: O(log n)
    """

    def __init__(self, data: list = [], cmp: callable = None) -> None:
        self.data = data
        self.cmp = cmp if cmp else lambda x, y: x < y
        self.build_heap()

    def build_heap(self) -> None:
        """
        Converts the data list into a binary minimum heap.
        """
        for i in range(len(self.data) // 2, -1, -1):
            self.heapify(self.data, i)

    def heapify(self, data: list, i: int) -> None:
        """
        Heapifies the subtree rooted at index i.
        """
        prnt = i
        l = left(i)
        r = right(i)

        # determine which node should be the parent
        if l < len(data) and self.cmp(data[l], data[prnt]):
            prnt = l
        if r < len(data) and self.cmp(data[r], data[prnt]):
            prnt = r

        # change parent if necessary and fix subree
        if prnt != i:
            data[i], data[prnt] = data[prnt], data[i]
            self.heapify(data, prnt)

    def peek_top(self):
        if self.is_empty():
            return None

        return self.data[0]

    def extract_top(self):
        """
        Extracts the top element from the heap.
        """
        if self.is_empty():
            return None

        top = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.heapify(self.data, 0)
        return top

    def insert(self, key) -> None:
        """
        Inserts a new key into the heap.
        """
        self.data.append(key)
        i = len(self.data) - 1
        prnt = parent(i)

        while i > 0 and self.cmp(self.data[i], self.data[prnt]):
            self.data[i], self.data[prnt] = self.data[prnt], self.data[i]
            i = prnt
            prnt = parent(i)

    def is_empty(self):
        return len(self.data) == 0
