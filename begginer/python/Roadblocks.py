import sys
from collections import deque
import copy
import heapq


def main():
    N, R = map(int, input().split())
    dp = [[] for i in range(N)]
    d = [[10 ** 9, 10 ** 9] for i in range(N)]
    heap = []
    for i in range(R):
        a, b, distance = map(int, input().split())
        a -= 1
        b -= 1
        dp[a].append((b, distance))
        dp[b].append((a, distance))
    heapq.heappush(heap, (0, 0))
    d[0][0] = 0
    while len(heap) != 0:
        distance, now_v = heapq.heappop(heap)
        if d[now_v][1] < distance:
            continue
        for i in range(len(dp[now_v])):
            next_v = dp[now_v][i][0]
            edge_cost = dp[now_v][i][1]
            if d[next_v][0] > distance + edge_cost:
                d[next_v][1] = d[next_v][0]
                d[next_v][0] = distance + edge_cost
                heapq.heappush(heap, (d[next_v][0], next_v))
            if d[next_v][1] > distance + edge_cost and d[next_v][0] < distance + edge_cost:
                d[next_v][1] = distance + edge_cost
                heapq.heappush(heap, (d[next_v][1], next_v))
    print(d[N - 1][1])
            


if __name__ == '__main__':
    main()
