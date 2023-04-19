# How to use:

## Creating a Graph

### Simple undirected graph with 4 vertices
**method one:**
```
graph1 = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [0]
}

g = Graph(graph1)
```
**method two:**
```
g = Graph(4)

# from, to
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 0)
```

### A directed and weighted graph with 4 vertices
**method one:**
```
graph2 = {
    0: [[1, 5], [2, 3]],
    1: [[3, 8]],
    2: [[3, 6]],
    3: [[0, 4]]
}

g = Graph(graph2, isDirected=True)
```
**method two:**
```
g = Graph(4, isDirected=True)

# from, to, weight
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(2, 3, 6)
g.add_edge(3, 0, 4)
```


## Search algorithms
They all return a path from point **A** to point **B**.
If it returns `[]` then the path doesn't exist

### Breadth-first search (BFS)
<img src="https://upload.wikimedia.org/wikipedia/commons/f/f5/BFS-Algorithm_Search_Way.gif" width="250" height="250"><br>
Used for finding the shortest path a maze
```
g.BFS(0, 3)
```

### Depth-first search (DFS)
<img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif" width="250" height="250"><br>
Used for searching trees
```
g.DFS(0, 3)
```

### Dijkstra's algorithm
<img src="https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif" width="250" height="250"><br>
Used for finding the shortest path in a weighted graph
```
g.Dijkstra(0, 3)
```

### A* algorithm
<img src="https://upload.wikimedia.org/wikipedia/commons/5/5d/Astar_progress_animation.gif" width="250" height="250"><br>
Used for finding the shortest path around an obstacle<br><br>
**this algorithm has a SEPERATE library** `AStar.py`
```
    maze: list[list[bool]] = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
    
    start: tuple[int] = (0, 0)  # Y, X
    end: tuple[int] = (0, 9)    # Y, X

    m = Maze(maze, diagonalMovement=False)
    path: list[tuple[int]] = m.astar(start, end)
```