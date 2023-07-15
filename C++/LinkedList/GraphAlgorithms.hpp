#include <vector>
#include <unordered_map>

#pragma once

// ===================================== EDGE =====================================

struct Edge {
    int vertex;
    int weigth;
    Edge(int v, int w) : vertex(v), weigth(w) {}
};

// ===================================== GRAPH CLASS =====================================

class Graph {
public:
    int vertexCount;                            // number of vertices
    bool isDirected;                            // wherther a graph is directed or not
    std::vector<std::vector<Edge>> verticies;   // the structure of the graph

    // ---------------------------- CLASS MANIPULATION ----------------------------
    // create a graph by the number of verticies
    Graph(int vertexCount, bool isDirected){
        this->isDirected = isDirected;
        this->vertexCount = vertexCount;
        this->verticies = std::vector<std::vector<Edge>>(vertexCount, std::vector<Edge>());
    }

    // create an undirected graph from HashMap
    Graph(std::unordered_map<int, std::vector<int>> graph){
        this->isDirected = false;
        this->vertexCount = graph.size();
        this->verticies = std::vector<std::vector<Edge>>(vertexCount, std::vector<Edge>());

        for(auto vertex : graph){
            for(int edge : vertex.second){

            }
        }
    }

    // add unweighted edge
    void addEdge(int a, int b) {
        verticies[a].push_back(Edge(b, 0));
        if(!isDirected) verticies[b].push_back(Edge(a, 0));
    }

    // add weighted edge
    void addEdge(int a, int b, int weigth) {
        verticies[a].push_back(Edge(b, weigth));
        if(!isDirected) verticies[b].push_back(Edge(a, weigth));
    }
    






};