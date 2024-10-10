// Implement Dijkstras algorithm to find the shortest path from one node to all other nodes in a graph with non-negative edge weights.
// 
// Kattis only asks for the shortest distance while your solution should be able to construct the actual shortest paths.
// 
// Suggested API:
// distance/parent[] shortest_path(graph G, node start) 
//


// function Dijkstra(Graph, source):
//    
//     for each vertex v in Graph.Vertices:
//         dist[v] ← INFINITY
//         prev[v] ← UNDEFINED
//         add v to Q
//     dist[source] ← 0
//    
//     while Q is not empty:
//         u ← vertex in Q with minimum dist[u]
//         remove u from Q
//        
//         for each neighbor v of u still in Q:
//             alt ← dist[u] + Graph.Edges(u, v)
//             if alt < dist[v]:
//                 dist[v] ← alt
//                 prev[v] ← u
//
//     return dist[], prev[]


