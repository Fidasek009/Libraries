# How to use:

## Creating a Graph

### Simple undirected graph with 4 vertices
**method one:**
```
std::vector<std::vector<int>> graph1{
    {1, 2},
    {3},
    {3},
    {0}
};

Graph g1 = Graph(graph1);
```
**method two:**
```
Graph g1 = Graph(4);

// from, to
g1.addEdge(0, 1);
g1.addEdge(0, 2);
g1.addEdge(1, 3);
g1.addEdge(2, 3);
g1.addEdge(3, 0);
```

### A directed and weighted graph with 4 vertices
**method one:**
```
std::vector<std::vector<std::vector<int>>> graph2{
    {{1, 5}, {2, 3}},
    {{3, 8}},
    {{3, 6}},
    {{0, 4}}
};

Graph g2 = Graph(graph2, true);
```
**method two:**
```
Graph g2 = Graph(4, true);

// from, to, weight
g2.addEdge(0, 1, 5);
g2.addEdge(0, 2, 3);
g2.addEdge(1, 3, 8);
g2.addEdge(2, 3, 6);
g2.addEdge(3, 0, 4);
```


## Search algorithms
They all return a path from point **A** to point **B**.
If it returns *empty vector* then the path doesn't exist

### Breadth-first search (BFS)
<img src="https://upload.wikimedia.org/wikipedia/commons/f/f5/BFS-Algorithm_Search_Way.gif" width="250" height="250"><br>
Used for finding the shortest path a maze
```
std::vector<int> path = g.BFS(0, 3);
```

### Depth-first search (DFS)
<img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif" width="250" height="250"><br>
Used for searching trees
```
std::vector<int> path = g.DFS(0, 3);
```

### Dijkstra's algorithm
<img src="https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif" width="250" height="250"><br>
Used for finding the shortest path in a weighted graph
```
std::vector<int> path = g.Dijkstra(0, 3);
```