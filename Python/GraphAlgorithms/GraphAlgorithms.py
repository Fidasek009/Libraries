from typing import List, Union

INF = float('inf')

# ===================================== EDGE CLASS =====================================
class Edge:
    vertex: int
    weight: int


    def __init__(self, v: int, w: int):
        self.vertex = v
        self.weight = w

# ===================================== GRAPH CLASS =====================================

class Graph():
    vertex_count: int           # number of vertices
    isDirected: bool            # wherther a graph is directed or not
    vertices: List[List[Edge]]  # the structure of the graph


    # --------------------------------- CLASS MANIPULATION ---------------------------------
    # constructor
    def __init__(self, vertexes: Union[int, dict[List[List[int]]], dict[List[int]]], isDirected: bool = False) -> None:
        self.isDirected = isDirected
        if type(vertexes) == int:
            self.vertex_count = vertexes
            self.vertices = [[] for i in range(vertexes)]
        else:
            self.vertex_count = len(vertexes)
            self.build(vertexes)


    # overrides string to print the class
    def __str__(self) -> str:
        s = "VERTEX -> (VERTEX|WEIGHT)\n"
        for i in range(self.vertex_count):
            s += str(i) + " -> "
            for edge in self.vertices[i]:
                s += "(" + str(edge.vertex) + "|" + str(edge.weight) + "), "
            s += "\n"
        
        return s


    # --------------------------------- ADD/REMOVE EDGE ---------------------------------
    def add_edge(self, a: int, b: int, weight: int = 1) -> None:
        self.vertices[a].append(Edge(b, weight))
        if not self.isDirected: # reverse the direction
            self.vertices[b].append(Edge(a, weight))


    def delete_edge(self, a: int, b: int) -> None:
        for edge in self.vertices[a]:
            if edge.vertex == b: 
                self.vertices[a].remove(edge)
        
        if not self.isDirected:
            for edge in self.vertices[b]:
                if edge.vertex == a: 
                    self.vertices[b].remove(edge)


    # --------------------------------- BUILD GRAPH ---------------------------------
    def build(self, graph: Union[dict[List[List[int]]], dict[List[int]]]) -> None:
        self.vertices = [[] for _ in range(self.vertex_count)]
        for vertex in graph:
            for edge in graph[vertex]:
                try:
                    self.add_edge(vertex, edge[0], edge[1]) # weighted edge
                except:
                    self.add_edge(vertex, edge) # unweighted edge   


    # --------------------------------- FIND PATH IN TREE ---------------------------------
    def Path(self, start: int, finish: int, tree: List[int]) -> List[int]:
        path: List[int] = []

        if tree[finish] != -1:  # start != finish
            while finish != start:
                path.append(finish)
                finish = tree[finish]
            path.append(start)
            path.reverse()

        return path


    # --------------------------------- BREADTH FIRST SEARCH ---------------------------------
    def BFS_tree(self, start: int) -> List[int]:
        visited: List[bool] = [False for _ in range(self.vertex_count)]
        tree: List[int] = [-1 for _ in range(self.vertex_count)]
        queue: List[int] = []
        v: int # current vertex

        visited[start] = True
        queue.append(start) # put the start in the queue

        while queue:
            v = queue.pop(0)

            for edge in self.vertices[v]:
                if not visited[edge.vertex]:
                    visited[edge.vertex] = True
                    tree[edge.vertex] = v
                    queue.append(edge.vertex)

        return tree
    

    def BFS(self, start: int, finish: int) -> List[int]:
        tree: List[int] = self.BFS_tree(start) # get the tree from BFS algorithm
        return self.Path(start, finish, tree)


    # --------------------------------- DEPTH FIRST SEARCH ---------------------------------
    def DFS_tree(self, start: int) -> List[int]:
        visited: List[bool] = [False for _ in range(self.vertex_count)]
        tree: List[int] = [-1 for _ in range(self.vertex_count)]
        stack: List[int] = []
        v: int # current vertex

        stack.append(start) # put the start in the stack

        while stack:
            v = stack.pop() # take the top item on stack

            if not visited[v]:
                visited[v] = True

                for edge in self.vertices[v]:
                    stack.append(edge.vertex)
                    if not visited[edge.vertex]: tree[edge.vertex] = v
            
        return tree


    def DFS(self, start: int, finish: int) -> List[int]:
        tree: List[int] = self.DFS_tree(start) # get the tree from DFS algorithm
        return self.Path(start, finish, tree)


    # --------------------------------- DIJKSTRA SEARCH ---------------------------------
    def Dijkstra_tree(self, start: int) -> List[int]:
        distance: List[int] = [INF for _ in range(self.vertex_count)] # distance from start node
        tree: List[int] = [-1 for _ in range(self.vertex_count)]
        queue: List[int] = []
        v: int # current vertex

        distance[start] = 0
        queue.append(start)

        while queue:
            v = queue.pop(0)

            for edge in self.vertices[v]:
                if distance[v] + edge.weight < distance[edge.vertex]:
                    distance[edge.vertex] = distance[v] + edge.weight
                    tree[edge.vertex] = v
                    queue.append(edge.vertex)
        
        return tree


    def Dijkstra(self, start: int, finish: int) -> List[int]:
        tree: List[int] = self.Dijkstra_tree(start) # get the tree from Dijkstra algorithm
        return self.Path(start, finish, tree)
    
    # --------------------------------- A* SEARCH ---------------------------------
    def AStar_tree(self, start: int) -> List[int]:
        # Nah bro i give up. (╯°□°）╯︵ ┻━┻
        # I've been staring at the screen for 2 hours watching an indian guy explain heuristic values. ༼ つ ◕_◕ ༽つ
        pass
