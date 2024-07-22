import heapq
import time


def dijkstra_v1(graph, start):
    pq = [(0, start)]
    shortest_paths = {start: (None, 0)}
    visited = set()

    while pq:
        (cost, node) = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor in visited:
                continue
            new_cost = cost + weight
            if neighbor not in shortest_paths or new_cost < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (node, new_cost)
                heapq.heappush(pq, (new_cost, neighbor))

    paths = {node: [] for node in shortest_paths}
    for node in shortest_paths:
        current = node
        while current is not None:
            paths[node].insert(0, current)
            current = shortest_paths[current][0]

    return paths, shortest_paths


class Node:
    def __init__(self):
        self.d = float("inf")
        self.parent = None
        self.finished = False


def dijkstra_v2(graph, source):
    nodes = {}
    for node in graph:
        nodes[node] = Node()
    nodes[source].d = 0
    pq = [(0, source)]

    while pq:
        d, node = heapq.heappop(pq)

        if nodes[node].finished:
            continue

        nodes[node].finished = True
        # 이 부분이 if dist[Vextracted] == dist_extracted 확인에 해당합니다.
        if d > nodes[node].d:
            continue

        for neighbor in graph[node]:
            if nodes[neighbor].finished:
                continue
            new_d = d + graph[node][neighbor]
            if new_d < nodes[neighbor].d:
                nodes[neighbor].d = new_d
                nodes[neighbor].parent = node
                heapq.heappush(pq, (new_d, neighbor))
    return nodes


graph1 = {
    "s": [("a", 8), ("b", 4), ("c", 7), ("d", 5), ("e", 10), ("f", 3)],
    "a": [("b", 4), ("e", 2), ("g", 9), ("h", 3)],
    "b": [("a", 3), ("c", 2), ("d", 5), ("f", 6), ("i", 7)],
    "c": [("d", 2), ("g", 3), ("j", 4), ("k", 1)],
    "d": [("h", 1), ("i", 3), ("k", 6)],
    "e": [("f", 1), ("j", 4), ("l", 2)],
    "f": [("g", 2), ("m", 3)],
    "g": [("h", 3), ("n", 2)],
    "h": [("i", 2), ("o", 3), ("p", 1)],
    "i": [("j", 4), ("k", 5), ("q", 2)],
    "j": [("r", 2)],
    "k": [("s", 3)],
    "l": [("t", 1)],
    "m": [("u", 3)],
    "n": [("v", 2)],
    "o": [("w", 1)],
    "p": [("x", 4)],
    "q": [("y", 2)],
    "r": [("z", 3)],
    "s": [("a1", 2)],
    "t": [("b1", 1)],
    "u": [("c1", 3)],
    "v": [("d1", 2)],
    "w": [("e1", 1)],
    "x": [("f1", 4)],
    "y": [("g1", 2)],
    "z": [("h1", 3)],
    "a1": [("i1", 2)],
    "b1": [("j1", 1)],
    "c1": [("k1", 3)],
    "d1": [("l1", 2)],
    "e1": [("m1", 1)],
    "f1": [("n1", 4)],
    "g1": [("o1", 2)],
    "h1": [("p1", 3)],
    "i1": [("q1", 2)],
    "j1": [("r1", 1)],
    "k1": [("s1", 3)],
    "l1": [("t1", 2)],
    "m1": [("u1", 1)],
    "n1": [("v1", 4)],
    "o1": [("w1", 2)],
    "p1": [("x1", 3)],
    "q1": [("y1", 2)],
    "r1": [("z1", 1)],
    "s1": {},
    "t1": {},
    "u1": {},
    "v1": {},
    "w1": {},
    "x1": {},
    "y1": {},
    "z1": {},
}

# Directed graph using a dictionary adjacency list
graph2 = {
    "s": {"a": 8, "b": 4, "c": 7, "d": 5, "e": 10, "f": 3},
    "a": {"b": 4, "e": 2, "g": 9, "h": 3},
    "b": {"a": 3, "c": 2, "d": 5, "f": 6, "i": 7},
    "c": {"d": 2, "g": 3, "j": 4, "k": 1},
    "d": {"h": 1, "i": 3, "k": 6},
    "e": {"f": 1, "j": 4, "l": 2},
    "f": {"g": 2, "m": 3},
    "g": {"h": 3, "n": 2},
    "h": {"i": 2, "o": 3, "p": 1},
    "i": {"j": 4, "k": 5, "q": 2},
    "j": {"r": 2},
    "k": {"s": 3},
    "l": {"t": 1},
    "m": {"u": 3},
    "n": {"v": 2},
    "o": {"w": 1},
    "p": {"x": 4},
    "q": {"y": 2},
    "r": {"z": 3},
    "s": {"a1": 2},
    "t": {"b1": 1},
    "u": {"c1": 3},
    "v": {"d1": 2},
    "w": {"e1": 1},
    "x": {"f1": 4},
    "y": {"g1": 2},
    "z": {"h1": 3},
    "a1": {"i1": 2},
    "b1": {"j1": 1},
    "c1": {"k1": 3},
    "d1": {"l1": 2},
    "e1": {"m1": 1},
    "f1": {"n1": 4},
    "g1": {"o1": 2},
    "h1": {"p1": 3},
    "i1": {"q1": 2},
    "j1": {"r1": 1},
    "k1": {"s1": 3},
    "l1": {"t1": 2},
    "m1": {"u1": 1},
    "n1": {"v1": 4},
    "o1": {"w1": 2},
    "p1": {"x1": 3},
    "q1": {"y1": 2},
    "r1": {"z1": 1},
    "s1": {},
    "t1": {},
    "u1": {},
    "v1": {},
    "w1": {},
    "x1": {},
    "y1": {},
    "z1": {},
}

# Even more complex graph
graph1_large = {
    "s": [("a", 8), ("b", 4), ("c", 7), ("d", 5), ("e", 10)],
    "a": [("b", 4), ("f", 2)],
    "b": [("a", 3), ("c", 2), ("d", 5), ("g", 6)],
    "c": [("d", 2), ("h", 3)],
    "d": [("i", 1)],
    "e": [("j", 2)],
    "f": [("g", 1), ("k", 5)],
    "g": [("h", 2), ("l", 4)],
    "h": [("i", 2), ("m", 3)],
    "i": [("n", 3)],
    "j": [("k", 4)],
    "k": [("l", 3)],
    "l": [("m", 1)],
    "m": [("n", 2)],
    "n": [("o", 1)],
    "o": [("p", 3)],
    "p": {},
}

graph2_large = {
    "s": {"a": 8, "b": 4, "c": 7, "d": 5, "e": 10},
    "a": {"b": 4, "f": 2},
    "b": {"a": 3, "c": 2, "d": 5, "g": 6},
    "c": {"d": 2, "h": 3},
    "d": {"i": 1},
    "e": {"j": 2},
    "f": {"g": 1, "k": 5},
    "g": {"h": 2, "l": 4},
    "h": {"i": 2, "m": 3},
    "i": {"n": 3},
    "j": {"k": 4},
    "k": {"l": 3},
    "l": {"m": 1},
    "m": {"n": 2},
    "n": {"o": 1},
    "o": {"p": 3},
    "p": {},
}


# Measure execution time of dijkstra_v1
start_time = time.time()
for i in range(100):
    dijkstra_v1(graph1, "s")

end_time = time.time()
print("dijkstra_v1 execution time:", end_time - start_time)


# Measure execution time of dijkstra_v2
start_time = time.time()

for i in range(100):
    dijkstra_v2(graph2, "s")

end_time = time.time()
print("dijkstra_v2 execution time:", end_time - start_time)
