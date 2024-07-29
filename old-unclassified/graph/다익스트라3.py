import time
import heapq


def dijkstra(graph, source, target):
    pq = []  # 우선순위 큐 (min-heap) 생성

    dist = {vertex: float("infinity") for vertex in graph}
    dist[source] = 0  # 시작 노드의 거리 초기화

    heapq.heappush(pq, (0, source))  # 시작노드를 pq에 추가

    # 이전 노드 추적용
    prev = {vertex: None for vertex in graph}

    while pq:
        # 최솟값을 가지는 노드 추출
        current_dist, u = heapq.heappop(pq)

        if u == target:
            break

        # if current_dist > dist[u]:  # 이미 처리된 노드는 무시
        #     # print("?", end=" ")
        #     continue

        for neighbor, weight in graph[u].items():
            alt = current_dist + weight
            # 새로운 최단 경로 발견 시 갱신
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u
                heapq.heappush(pq, (alt, neighbor))

    return dist, prev


graph = {
    "A": {"B": 1, "D": 2},
    "B": {"A": 1, "C": 1, "D": 2},
    "C": {"B": 1, "D": 2, "E": 3},
    "D": {"A": 2, "B": 2, "C": 2, "E": 1},
    "E": {"C": 3, "D": 1},
}


start_time = time.time()

# for i in range(100):
dist, prev = dijkstra(graph, "A", "E")

end_time = time.time()
print("dijkstraexecution time:", end_time - start_time)


# print("Distance from source:", dist)
# print("Previous node:", prev)
