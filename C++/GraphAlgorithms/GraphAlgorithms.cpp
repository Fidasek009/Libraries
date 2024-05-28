#include <vector>
#include <unordered_set>
#include <stack>
#include <queue>
#include <algorithm>
#include "GraphAlgorithms.hpp"


// ---------------------------- CLASS MANIPULATION ----------------------------
// create a graph by the number of vertices
Graph::Graph(int vertexes, bool directed) {
    vertexCount = vertexes;
    isDirected = directed;
    graph = std::vector<std::unordered_set<Edge, EdgeHash>>(vertexCount, std::unordered_set<Edge, EdgeHash>());
}

// create an unweighted graph from HashMap
Graph::Graph(std::vector<std::vector<int>> graph, bool directed){
    vertexCount = graph.size();
    isDirected = directed;
    this->graph = std::vector<std::unordered_set<Edge, EdgeHash>>(vertexCount, std::unordered_set<Edge, EdgeHash>());
    
    for(int i = 0; i < graph.size(); i++){
        for(int edge : graph[i]){
            if(edge+1 > vertexCount) throw std::invalid_argument("Vertex " + std::to_string(edge) + " doesn't exist");
            addEdge(i, edge);
            if(!directed) addEdge(edge, i);
        }
    }
}

// create a weighted graph from HashMap
Graph::Graph(std::vector<std::vector<std::vector<int>>> graph, bool directed){
    vertexCount = graph.size();
    isDirected = directed;
    this->graph = std::vector<std::unordered_set<Edge, EdgeHash>>(vertexCount, std::unordered_set<Edge, EdgeHash>());
    
    for(int i = 0; i < graph.size(); i++){
        for(std::vector<int> edge : graph[i]){
            if(edge[0]+1 > vertexCount) throw std::invalid_argument("Vertex " + std::to_string(edge[0]) + " doesn't exist");
            addEdge(i, edge[0], edge[1]);
            if(!directed) addEdge(edge[0], i, edge[1]);
        }
    }
}


// ---------------------------- ADD/REMOVE EDGE ----------------------------
void Graph::addEdge(int a, int b, int weigth) {
    graph[a].insert(Edge(b, weigth));
    if(!isDirected) graph[b].insert(Edge(a, weigth));
}

void Graph::removeEdge(int a, int b) {
    graph[a].erase(Edge(b, 1));
    if(!isDirected) graph[b].erase(Edge(a, 1));
}

// ---------------------------- FIND PATH IN TREE ----------------------------
std::vector<int> Graph::path(int start, int finish, std::vector<int> tree){
    std::vector<int> path;

    // there is no path
    if(tree[finish] == -1) return path;

    while(start != finish) {
        path.push_back(finish);
        finish = tree[finish];
    }

    path.push_back(start);
    std::reverse(path.begin(), path.end());
    return path;
}

// ---------------------------- BREADTH FIRST SEARCH ----------------------------
std::vector<int> Graph::BFSTree(int start) {
    std::vector<bool> visited(graph.size(), false);
    std::vector<int> tree(graph.size(), -1);
    std::queue<int> q;

    visited[start] = true;
    q.push(start);

    while(q.size() > 0){
        int v = q.front();
        q.pop();

        for(Edge edge : graph[v]){
            if(!visited[edge]){
                visited[edge] = true;
                tree[edge] = v;
                q.push(edge);
            }
        }
    }

    return tree;
}

std::vector<int> Graph::BFS(int start, int finish) {
    std::vector<int> tree = BFSTree(start);
    return path(start, finish, tree);
}

// ---------------------------- DEPTH FIRST SEARCH ----------------------------
std::vector<int> Graph::DFSTree(int start) {
    std::vector<bool> visited(graph.size(), false);
    std::vector<int> tree(graph.size(), -1);
    std::stack<int> s;

    visited[start] = true;
    s.push(start);

    while(s.size() > 0){
        int v = s.top();
        s.pop();

        for(Edge edge : graph[v]){
            if(!visited[edge]){
                visited[edge] = true;
                tree[edge] = v;
                s.push(edge);
            }
        }
    }

    return tree;
}

std::vector<int> Graph::DFS(int start, int finish) {
    std::vector<int> tree = DFSTree(start);
    return path(start, finish, tree);
}

// ---------------------------- DIJKSTRA'S ALGORITHM ----------------------------
std::vector<int> Graph::DijkstraTree(int start){
    std::vector<int> distance(graph.size(), INT_MAX);
    std::vector<int> tree(graph.size(), -1);
    std::priority_queue<int> pq;

    distance[start] = 0;
    pq.push(start);

    while(pq.size() > 0){
        int v = pq.top();
        pq.pop();

        for(Edge edge : graph[v]){
            if(distance[v] + edge.weigth < distance[edge]){
                distance[edge] = distance[v] + edge.weigth;
                tree[edge] = v;
                pq.push(edge);
            }
        }
    }

    return tree;
}

std::vector<int> Graph::Dijkstra(int start, int finish){
    std::vector<int> tree = DijkstraTree(start);
    return path(start, finish, tree);
}
