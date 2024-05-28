class Node:
    def __init__(self, leaf: bool = False) -> None:
        self.keys: list = []
        self.children: list[Node] = []
        self.leaf: bool = leaf


class BTree:
    """
    A basic B-tree implementation.
    The tree doesn't support duplicates.

    Attributes:
        root: The root of the tree.
        t: The minimum degree of the tree.
        min: The minimum number of keys in a node. (t - 1)
        max: The maximum number of keys in a node. (2t - 1)

    Methods:
        is_empty: O(1)
        node_bsearch: O(log t)
        search: O(log n)
        split: O(t)
        insert_nonfull: O(log n)
        insert: O(log n)
        delete: O(log n) TODO
    """

    def __init__(self, t: int) -> None:
        self.root = Node(leaf=True)
        self.t = t
        self.min = t - 1
        self.max = 2 * t - 1

    def is_empty(self) -> bool:
        return not self.root.keys

    def node_bsearch(self, node: Node, key) -> int:
        """
        Finds the index of the first key in the node
        that is >= to the given key.
        """
        low = 0
        high = len(node.keys)

        while low < high:
            mid = (low + high) // 2
            if key > node.keys[mid]:
                low = mid + 1
            else:
                high = mid

        return low

    def search(self, node: Node, key) -> tuple[Node, int] | None:
        # find index >= key
        i = self.node_bsearch(node, key)

        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
        if node.leaf:
            return None
        return self.search(node.children[i], key)

    def split(self, node: Node, i: int) -> None:
        """
        Split the child node of the given node at index i.
        """
        # old node to split
        full_node = node.children[i]
        # new node that takes half the keys
        new_node = Node(leaf=full_node.leaf)

        # split the keys into two parts
        new_node.keys = full_node.keys[self.t:]
        full_node.keys = full_node.keys[:self.t]

        # split the children if the child is not a leaf
        if not full_node.leaf:
            new_node.children = full_node.children[self.t:]
            full_node.children = full_node.children[:self.t]

        # insert the new node to the parent's children
        node.children.insert(i + 1, new_node)
        # take last key from the full node and insert it to the parent
        node.keys.insert(i, full_node.keys.pop())

    def insert_nonfull(self, node: Node, key) -> None:
        """
        Insert a key to a non-full node.
        """
        i = self.node_bsearch(node, key)

        # only insert into leaf nodes
        if node.leaf:
            node.keys.insert(i, key)
            return

        # preemtively split the child if it's full
        if len(node.children[i].keys) == self.max:
            self.split(node, i)
            if key > node.keys[i]:
                i += 1

        self.insert_nonfull(node.children[i], key)

    def insert(self, key) -> None:
        """
        Insert a key into the tree.
        """
        # split the root if it's full
        if len(self.root.keys) == self.max:
            full_node = self.root
            self.root = Node()
            self.root.children.append(full_node)
            self.split(self.root, 0)

        self.insert_nonfull(self.root, key)
