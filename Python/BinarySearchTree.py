class Node:
    def __init__(self, key):
        self.key = key
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None


class BinarySearchTree:
    """
    A basic implementation of a binary search tree.
    The tree isn't balanced and doesn't support duplicates.

    Attributes:
        root: The root of the tree.

    Methods:
        is_empty: O(1)
        insert: O(h)
        search: O(h)
        min: O(h)
        max: O(h)
        transplant: O(1)
        delete: O(h)
        predecessor: O(h)
        successor: O(h)
        preorder: O(n)
        inorder: O(n)
        postorder: O(n)
    """
    def __init__(self) -> None:
        self.root: Node | None = None

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, key) -> None:
        parent = None
        current = self.root

        # find parent of the new node
        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        node = Node(key)
        node.parent = parent

        # insert the new node
        if parent is None:
            self.root = node
        elif key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def search(self, key) -> Node | None:
        node = self.root

        while node is not None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return node

    def min(self, node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node

    def max(self, node: Node) -> Node:
        while node.right is not None:
            node = node.right
        return node

    def transplant(self, u: Node, v: Node | None) -> None:
        """
        Replaces the subtree rooted at node u
        with the subtree rooted at node v.

        (replaces the parent link, removes u subtree from the tree)
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def delete(self, node: Node) -> None:
        if node.left is None:
            return self.transplant(node, node.right)
        if node.right is None:
            return self.transplant(node, node.left)

        # node has two children → find the successor
        # 💡succesor never has a left child
        succs = self.min(node.right)

        # successor in't the right child of the node
        if succs.parent != node:
            # remove the successor from its current position
            self.transplant(succs, succs.right)
            # fix the successor's right link
            succs.right = node.right
            succs.right.parent = succs

        # replace the node with its successor
        self.transplant(node, succs)
        # fix the successor's left link
        succs.left = node.left
        succs.left.parent = succs

    def predecessor(self, node: Node) -> Node | None:
        """
        Predecessor is the node with the largest key smaller than node.
        """
        # predecessor is the max in the left subtree
        if node.left is not None:
            return self.max(node.left)

        # go up until the node isn't a left child of parent
        parent = node.parent
        while parent is not None and node == parent.left:
            node = parent
            parent = parent.parent

        return parent

    def successor(self, node: Node) -> Node | None:
        """
        Successor is the node with the smallest key larger than node.
        """
        # successor is the min in the right subtree
        if node.right is not None:
            return self.min(node.right)

        # go up until the node isn't a right child of parent
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent

        return parent

    def preorder(self, node: Node, res: list) -> None:
        if node is None:
            return

        res.append(node.key)
        self.preorder(node.left, res)
        self.preorder(node.right, res)

    def inorder(self, node: Node, res: list) -> None:
        if node is None:
            return

        self.inorder(node.left, res)
        res.append(node.key)
        self.inorder(node.right, res)

    def postorder(self, node: Node, res: list) -> None:
        if node is None:
            return

        self.postorder(node.left, res)
        self.postorder(node.right, res)
        res.append(node.key)


def build_tree_postorder(tree: list, low: int, high: int) -> Node | None:
    """
    Builds a binary search tree from postorder traversal.
    """
    if low >= high:
        return None

    root = Node(tree[high - 1])
    i = low
    while i < high and tree[i] < root.key:
        i += 1

    root.left = build_tree_postorder(tree, low, i)
    root.right = build_tree_postorder(tree, i, high - 1)
    if root.left:
        root.left.parent = root
    if root.right:
        root.right.parent = root

    return root
