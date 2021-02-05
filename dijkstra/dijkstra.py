# 시작점에서 모든 정점까지 최소거리 구하기

# 시작점은 1이 기준
# 방향이 없는 경우가 기준
# 아래 구현한 함수는 거리가 K이하일 경우에만 구함

def solution(N, road, K):
    graph = collections.defaultdict(list)
    for a, b, dist in road:
        graph[a].append((b, dist))
        graph[b].append((a, dist))  # 방향이 없으므로
    
    dist = collections.defaultdict(int)  # 시작정점으로부터의 거리
    heap = [(0, 1)] # (거리, 시작 정점)
    
    while heap:
        w, v = heapq.heappop(heap)
        if v not in dist and w <= K:
            dist[v] = w
            for node, alt in graph[v]:
                heapq.heappush(heap, (w+alt, node))
    
    return len(dist)  # 문제조건 보면 시작점도 포함
