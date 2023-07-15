#include "GraphAlgorithms.hpp"
#include <vector>
#include <iostream>

int main(int argc, char const *argv[])
{
    // unweighted graph
    std::vector<std::vector<int>> graph1{
        {1, 2},
        {3},
        {3},
        {0}
    };
    Graph g1 = Graph(graph1);
    std::cout << "Unweighted:" << std::endl << g1 << std::endl;

    // weighted graph
    std::vector<std::vector<std::vector<int>>> graph2{
        {{1, 5}, {2, 3}},
        {{3, 8}},
        {{3, 6}},
        {{0, 4}}
    };
    Graph g2 = Graph(graph2, true);
    std::cout << "Weighted:" << std::endl << g2 << std::endl;

    // test BFS
    std::cout << "BFS: ";
    std::vector<int> bfs = g1.BFS(0, 3);
    for(int i : bfs) std::cout << i << " ";
    std::cout << std::endl;

    // test DFS
    std::cout << "DFS: ";
    std::vector<int> dfs = g1.DFS(0, 3);
    for(int i : dfs) std::cout << i << " ";
    std::cout << std::endl;

    // test Dijkstra
    std::cout << "Dijkstra: ";
    std::vector<int> dijkstra = g2.Dijkstra(0, 3);
    for(int i : dijkstra) std::cout << i << " ";
    std::cout << std::endl;

    return 0;
}
