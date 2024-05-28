from heapq import heapify, heappop
from time import time


def bubble_sort(arr: list):
    """
    O(n^2), stable, in-place

    Swaps adjacent elements if they are in the wrong order.
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


def selection_sort(arr: list):
    """
    O(n^2), stable, in-place

    Selects min element from the unsorted part.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr: list):
    """
    O(n^2), stable, in-place

    Inserts elements into the sorted part.
    """
    for i in range(1, len(arr)):
        # swap element until in correct place
        while 0 < i and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


def heap_sort(arr: list):
    """
    O(n log n), not stable, could be in-place

    Builds a heap and extracts the top element.
    """
    heap = arr.copy()
    heapify(heap)

    for i in range(len(arr)):
        arr[i] = heappop(heap)


def merge_sort(arr: list):
    """
    O(n log n), stable, not in-place

    Splits the array into two parts, sorts them and merges them.
    """
    def merge(arr: list, left: int, mid: int, right: int):
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        i = 0
        j = 0
        k = left

        # merge until one of the arrays is empty
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # merge remaining elements from left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # merge remaining elements from right
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    def merge_sort_aux(arr: list, left: int, right: int):
        if left >= right:
            return

        mid = (left + right) // 2
        merge_sort_aux(arr, left, mid)
        merge_sort_aux(arr, mid + 1, right)
        merge(arr, left, mid, right)

    merge_sort_aux(arr, 0, len(arr) - 1)


def quick_sort(arr: list):
    """
    O(n log n), not stable, in-place

    Picks a pivot and partitions the array around it.
    """
    def partition(arr: list, low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_aux(arr: list, low: int, high: int):
        if low >= high:
            return

        pi = partition(arr, low, high)
        quick_sort_aux(arr, low, pi - 1)
        quick_sort_aux(arr, pi + 1, high)

    quick_sort_aux(arr, 0, len(arr) - 1)


def counting_sort(arr: list[int]):
    """
    O(n + k), could be stable, not in-place

    ⚠️ Only works for non-negative integers.
    Counts the number of elements and reconstructs the array.
    """
    k = max(arr) + 1
    count = [0] * k

    for num in arr:
        count[num] += 1

    idx = 0
    for i, c in enumerate(count):
        for _ in range(c):
            arr[idx] = i
            idx += 1


def benchmark(arr: list, algorithms: list[callable]):
    """
    Compares the performance of different sorting algorithms.
    """
    print(f"Benchmarking on {format(len(arr), ',')} elements:")

    for algorithm in algorithms:
        start = time()
        algorithm(arr.copy())
        print(f"\t{algorithm.__name__}: {time() - start:.6f}s")
