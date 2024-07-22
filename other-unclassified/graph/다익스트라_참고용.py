import heapq


def dijkstra(graph, start):
    pq = [(0, start)]  # Priority queue to store (cost, node) tuples
    shortest_paths = {
        start: (None, 0)
    }  # Dictionary to store the shortest path to each node
    dist = {start: 0}
    visited = set()  # Set to store visited nodes

    while pq:
        (cost, node) = heapq.heappop(pq)

        if node in visited:
            print(node, end=" ")
            continue

        # if node in visited and cost > dist[node]:
        #     continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor in visited:
                continue
            new_cost = cost + weight
            if neighbor not in shortest_paths or new_cost < shortest_paths[neighbor][1]:
                dist[neighbor] = new_cost
                shortest_paths[neighbor] = (node, new_cost)
                heapq.heappush(pq, (new_cost, neighbor))

    # Reconstruct the paths
    paths = {node: [] for node in shortest_paths}
    for node in shortest_paths:
        current = node
        while current is not None:
            paths[node].insert(0, current)
            current = shortest_paths[current][0]

    return shortest_paths


# Example usage:
graph = {
    "A": [("B", 10), ("C", 3)],
    "B": [("C", 1), ("D", 2)],
    "C": [("B", 4), ("D", 8), ("E", 2)],
    "D": [("E", 7)],
    "E": [("D", 9)],
}

start_node = "A"
shortest_paths = dijkstra(graph, start_node)
print("Shortest Paths:", shortest_paths)
