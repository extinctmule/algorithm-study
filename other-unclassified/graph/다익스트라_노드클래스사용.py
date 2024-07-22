# https://builtin.com/software-engineering-perspectives/dijkstras-algorithm
import heapq


class Node:
    def __init__(self):
        self.d = float("inf")
        self.parent = None
        self.finished = False


def dijkstra(graph, source):
    nodes = {}
    for node in graph:
        nodes[node] = Node()
    nodes[source].d = 0
    pq = [(0, source)]  # priority queue

    while pq:
        d, node = heapq.heappop(pq)

        if nodes[node].finished:
            continue

        if d > nodes[node].d:
            continue
        nodes[node].finished = True

        for neighbor in graph[node]:
            if nodes[neighbor].finished:
                continue
            new_d = d + graph[node][neighbor]
            if new_d < nodes[neighbor].d:
                nodes[neighbor].d = new_d
                nodes[neighbor].parent = node
                heapq.heappush(pq, (new_d, neighbor))
    return nodes


# directed graph using a dictionary adjacency list
graph = {
    "s": {"a": 8, "b": 4},
    "a": {"b": 4},
    "b": {"a": 3, "c": 2, "d": 5},
    "c": {"d": 2},
    "d": {},
}

res = dijkstra(graph, "s")
