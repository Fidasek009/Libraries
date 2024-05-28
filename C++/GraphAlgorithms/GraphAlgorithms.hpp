#include <vector>
#include <unordered_set>
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
    Graph(int vertexes, bool directed = false);

    // create an unweighted graph from HashMap
    Graph(std::vector<std::vector<int>> graph, bool directed = false);

    // create a weighted graph from HashMap
    Graph(std::vector<std::vector<std::vector<int>>> graph, bool directed = false);

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
    void addEdge(int a, int b, int weigth = 1);
    void removeEdge(int a, int b);

    // ---------------------------- FIND PATH IN TREE ----------------------------
    std::vector<int> path(int start, int finish, std::vector<int> tree);

    // ---------------------------- BREADTH FIRST SEARCH ----------------------------
    std::vector<int> BFSTree(int start);
    std::vector<int> BFS(int start, int finish);

    // ---------------------------- DEPTH FIRST SEARCH ----------------------------
    std::vector<int> DFSTree(int start);
    std::vector<int> DFS(int start, int finish);

    // ---------------------------- DIJKSTRA'S ALGORITHM ----------------------------
    std::vector<int> DijkstraTree(int start);
    std::vector<int> Dijkstra(int start, int finish);
};
