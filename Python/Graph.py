from collections import deque           # queue for BFS
from heapq import heappop, heappush     # priority queue for Dijkstra

INF = float("inf")


class Graph:
    """
    A basic graph implementation.

    Attributes:
        n: The number of nodes in the graph.
        directed: Whether the graph is directed.
        edges: The adjacency list of the graph.

    Methods:
        add_edge: O(1)
        get_path: O(v)
        BFS_tree: O(v + e)
        DFS_tree: O(v + e)
    """
    def __init__(self, size: int, directed=False):
        self.n = size
        self.directed = directed
        self.edges = [[] for _ in range(size)]

    def add_edge(self, u, v):
        self.edges[u].append(v)
        if not self.directed:
            self.edges[v].append(u)

    def get_path(self, end: int, tree: list[int]) -> list[int]:
        """
        Recovers the path from the BFS/DFS tree.
        """
        path = []

        while end != -1:
            path.append(end)
            end = tree[end]

        return path[::-1]

    def bfs_tree(self, start: int, end: int = -1) -> list[int]:
        """
        Returns the BFS tree of the graph starting from `start`.
        Optionally terminate upon reaching `end` if specified.
        """
        tree = [-1 for _ in range(self.n)]
        visited = [False for _ in range(self.n)]
        visited[start] = True
        q: deque[int] = deque([start])

        while q:
            u = q.popleft()

            for v in self.edges[u]:
                if visited[v]:
                    continue

                visited[v] = True
                tree[v] = u
                q.append(v)

                if v == end:
                    break

        return tree

    def dfs_tree(self, start: int, end: int = -1) -> list[int]:
        """
        Returns the DFS tree of the graph starting from `start`.
        Optionally terminate upon reaching `end` if specified.
        """
        tree = [-1 for _ in range(self.n)]
        visited = [False for _ in range(self.n)]
        visited[start] = True
        stack = [start]

        while stack:
            u = stack.pop()

            for v in self.edges[u]:
                if visited[v]:
                    continue

                visited[v] = True
                tree[v] = u
                stack.append(v)

                if v == end:
                    break

        return tree


class WeightedGraph(Graph):
    """
    A basic weighted graph implementation.

    Attributes:
        n: The number of nodes in the graph.
        directed: Whether the graph is directed.
        edges: The adjacency list of the graph.
        weights: The weights of the edges.

    Methods:
        add_edge: O(1)
        Dijkstra_tree: O((v + e) · log v)
        BellmanFord_tree: O(v · e)
    """

    def __init__(self, size: int, directed=False):
        super().__init__(size, directed)
        self.weights = [[] for _ in range(size)]

    def add_edge(self, u, v, w):
        super().add_edge(u, v)
        self.weights[u].append(w)
        if not self.directed:
            self.weights[v].append(w)

    def dijkstra_tree(self, start: int, end: int = -1) -> list[int]:
        """
        Returns the Dijkstra tree of the graph starting from `start`.
        Optionally terminate upon reaching `end` if specified.
        """
        tree = [-1 for _ in range(self.n)]
        dist = [INF for _ in range(self.n)]
        dist[start] = 0
        pq = [(0, start)]

        while pq:
            d, u = heappop(pq)

            # already found a better distance
            if d > dist[u]:
                continue

            if u == end:
                break

            for i, v in enumerate(self.edges[u]):
                w = self.weights[u][i]

                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    tree[v] = u
                    heappush(pq, (dist[v], v))

        return tree

    def bellman_ford_tree(self, start: int) -> list[int] | None:
        """
        Returns the Bellman-Ford tree of the graph starting from `start`.
        If a negative cycle is detected, returns None.
        """
        tree = [-1 for _ in range(self.n)]
        dist = [INF for _ in range(self.n)]
        dist[start] = 0

        for _ in range(self.n - 1):
            for u in range(self.n):
                for i, v in enumerate(self.edges[u]):
                    w = self.weights[u][i]

                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        tree[v] = u

        # detect negative cycle
        for u in range(self.n):
            for i, v in enumerate(self.edges[u]):
                w = self.weights[u][i]

                if dist[u] + w < dist[v]:
                    return None

        return tree
