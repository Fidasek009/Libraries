#include <vector>
#include <unordered_set>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>

#pragma once

// ===================================== EDGE =====================================

struct Edge {
    int vertex;
    int weigth;
    Edge(int v, int w) : vertex(v), weigth(w) {}

    // int representation
    operator int() const {
        return vertex;
    }

    // comparing two edges
    bool operator == (const Edge& other) const {
        return vertex == other.vertex;
    }
};

// a hash function used to hash `Edge`
struct EdgeHash {
    std::size_t operator()(const Edge& edge) const {
        return std::hash<int>()(edge.vertex);
    }
};

// ===================================== GRAPH CLASS =====================================

class Graph {
public:
    int vertexCount;    // the number of vertices in a graph
    bool isDirected;    // wherther a graph is directed or not
    std::vector<std::unordered_set<Edge, EdgeHash>> graph;  // the structure of the graph

    // ---------------------------- CLASS MANIPULATION ----------------------------
    // create a graph by the number of vertices
    Graph(int vertexes, bool directed = false) {
        vertexCount = vertexes;
        isDirected = directed;
        graph = std::vector<std::unordered_set<Edge, EdgeHash>>(vertexCount, std::unordered_set<Edge, EdgeHash>());
    }

    // create an unweighted graph from HashMap
    Graph(std::vector<std::vector<int>> graph, bool directed = false){
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
    Graph(std::vector<std::vector<std::vector<int>>> graph, bool directed = false){
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

    // a string representation of the graph
    friend std::ostream& operator << (std::ostream& os, const Graph& obj) {
        for(int i = 0; i < obj.graph.size(); i++){
            os << i << " ->";
            for(Edge edge : obj.graph[i]){
                os << " (" << edge.vertex << "|" << edge.weigth << ")";
            }
            os << std::endl;
        }
        return os;
    }

    // ---------------------------- ADD/REMOVE EDGE ----------------------------
    void addEdge(int a, int b, int weigth = 1) {
        graph[a].insert(Edge(b, weigth));
        if(!isDirected) graph[b].insert(Edge(a, weigth));
    }

    void removeEdge(int a, int b) {
        graph[a].erase(Edge(b, 1));
        if(!isDirected) graph[b].erase(Edge(a, 1));
    }

    // ---------------------------- FIND PATH IN TREE ----------------------------
    std::vector<int> path(int start, int finish, std::vector<int> tree){
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
    std::vector<int> BFSTree(int start) {
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

    std::vector<int> BFS(int start, int finish) {
        std::vector<int> tree = BFSTree(start);
        return path(start, finish, tree);
    }

    // ---------------------------- DEPTH FIRST SEARCH ----------------------------
    std::vector<int> DFSTree(int start) {
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

    std::vector<int> DFS(int start, int finish) {
        std::vector<int> tree = DFSTree(start);
        return path(start, finish, tree);
    }

    // ---------------------------- DIJKSTRA'S ALGORITHM ----------------------------
    std::vector<int> DijkstraTree(int start){
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

    std::vector<int> Dijkstra(int start, int finish){
        std::vector<int> tree = DijkstraTree(start);
        return path(start, finish, tree);
    }
};