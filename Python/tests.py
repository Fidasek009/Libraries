from Queue import Queue
from Stack import Stack
from DoublyLinkedList import DoublyLinkedList
from Heap import Heap, cmp_max
from BinarySearchTree import BinarySearchTree
from BTree import BTree
from Graph import Graph, WeightedGraph
from Sort import bubble_sort, selection_sort, insertion_sort, heap_sort, \
                 merge_sort, quick_sort, counting_sort, benchmark
from random import randint


def test_sort():
    # generate random arr
    n = 1000
    arr = [randint(0, n) for _ in range(n)]
    sorted_arr = sorted(arr)

    # test individual sorting algorithms
    unsorted_arr = arr.copy()
    bubble_sort(unsorted_arr)
    assert unsorted_arr == sorted_arr

    unsorted_arr = arr.copy()
    selection_sort(unsorted_arr)
    assert unsorted_arr == sorted_arr

    unsorted_arr = arr.copy()
    insertion_sort(unsorted_arr)
    assert unsorted_arr == sorted_arr

    unsorted_arr = arr.copy()
    heap_sort(unsorted_arr)
    assert unsorted_arr == sorted_arr

    unsorted_arr = arr.copy()
    merge_sort(unsorted_arr)
    assert unsorted_arr == sorted_arr

    unsorted_arr = arr.copy()
    quick_sort(unsorted_arr)
    assert unsorted_arr == sorted_arr

    unsorted_arr = arr.copy()
    counting_sort(unsorted_arr)
    assert unsorted_arr == sorted_arr


def benchmark_sort():
    small_arr = [randint(0, 10000) for _ in range(10000)]
    slow_algorithms = [
        bubble_sort,
        selection_sort,
        insertion_sort,
    ]

    benchmark(small_arr, slow_algorithms)

    def python_sort(arr):
        arr.sort()

    large_arr = [randint(0, 1000000) for _ in range(1000000)]
    fast_algorithms = [
        heap_sort,
        merge_sort,
        quick_sort,
        counting_sort,
        python_sort,
    ]

    benchmark(large_arr, fast_algorithms)


def test_queue():
    q = Queue()

    assert q.is_empty()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert not q.is_empty()
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()


def test_stack():
    s = Stack()

    assert s.is_empty()
    s.push(1)
    s.push(2)
    s.push(3)
    assert not s.is_empty()
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()


def test_doubly_linked_list():
    dll = DoublyLinkedList()

    assert dll.is_empty()
    dll.push_back(1)
    dll.push_back(2)
    dll.push_back(3)
    assert not dll.is_empty()
    assert dll.head.key == 1
    assert dll.tail.key == 3
    assert dll.search(5) is None
    assert dll.search(2).key == 2
    dll.delete(dll.tail)
    assert dll.tail.key == 2
    dll.delete(dll.head)
    assert dll.head.key == 2
    dll.delete(dll.head)
    assert dll.search(2) is None
    assert dll.is_empty()


def test_heap():
    arr = list(range(1, 1000))
    h = Heap(arr, cmp_max)

    assert not h.is_empty()
    assert h.peek_top() == 999
    assert h.extract_top() == 999
    h.insert(1000)
    assert h.peek_top() == 1000
    assert h.extract_top() == 1000

    for i in range(998, 0, -1):
        assert h.extract_top() == i

    assert h.is_empty()


def test_binary_search_tree():
    bst = BinarySearchTree()

    assert bst.is_empty()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)

    #      5
    #     / \
    #    3   7
    #   / \
    #  2   4

    assert not bst.is_empty()
    assert bst.root.left.key == 3
    assert bst.root.right.key == 7
    assert bst.search(5).key == 5
    assert bst.search(3).key == 3
    assert bst.search(10) is None
    assert bst.min(bst.root).key == 2
    assert bst.max(bst.root).key == 7
    assert bst.successor(bst.root).key == 7
    assert bst.predecessor(bst.min(bst.root)) is None
    assert bst.predecessor(bst.root).key == 4
    assert bst.successor(bst.max(bst.root)) is None
    assert bst.successor(bst.root.left.left).key == 3
    bst.delete(bst.root.left)
    assert bst.search(3) is None
    bst.delete(bst.root)
    assert bst.search(5) is None
    assert not bst.is_empty()

    tree_arr = []
    bst.preorder(bst.root, tree_arr)
    assert tree_arr == [7, 4, 2]
    tree_arr = []
    bst.inorder(bst.root, tree_arr)
    assert tree_arr == [2, 4, 7]
    tree_arr = []
    bst.postorder(bst.root, tree_arr)
    assert tree_arr == [2, 4, 7]


def test_b_tree():
    btree = BTree(5)

    assert btree.is_empty()

    for i in range(1, 1000):
        btree.insert(i)

    assert not btree.is_empty()
    assert btree.search(btree.root, 1) is not None
    assert btree.search(btree.root, 999) is not None
    assert btree.search(btree.root, 500) is not None
    assert btree.search(btree.root, 1000) is None
    assert btree.search(btree.root, 0) is None


def test_unweighted_graph():
    g = Graph(10)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 8)
    g.add_edge(7, 9)

    t = g.bfs_tree(0)
    assert t == [-1, 0, 0, 1, 2, 3, 4, 5, 6, 7]
    assert g.get_path(9, t) == [0, 1, 3, 5, 7, 9]

    t = g.dfs_tree(0)
    assert t == [-1, 0, 0, 1, 2, 3, 4, 5, 6, 7]
    assert g.get_path(9, t) == [0, 1, 3, 5, 7, 9]


def test_weighted_graph():
    g = WeightedGraph(10, directed=True)

    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 6, 6)
    g.add_edge(5, 7, 7)
    g.add_edge(6, 8, 8)
    g.add_edge(7, 9, 9)

    t = g.dijkstra_tree(0)
    assert t == [-1, 0, 0, 1, 2, 3, 4, 5, 6, 7]
    assert g.get_path(9, t) == [0, 1, 3, 5, 7, 9]

    t = g.bellman_ford_tree(0)
    assert t == [-1, 0, 0, 1, 2, 3, 4, 5, 6, 7]
    assert g.get_path(9, t) == [0, 1, 3, 5, 7, 9]

    g.add_edge(9, 0, -100)
    t = g.bellman_ford_tree(0)
    assert t is None


if __name__ == "__main__":
    test_queue()
    test_stack()
    test_doubly_linked_list()
    test_heap()
    test_binary_search_tree()
    test_b_tree()
    test_unweighted_graph()
    test_weighted_graph()
    test_sort()
    print("All tests passed!")
    print("Benchmarking sorting algorithms...")
    benchmark_sort()
