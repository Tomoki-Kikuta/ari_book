import heapq


def main():
    n = int(input())
    l = [int(i) for i in input().split()]
    heap = []
    cost = 0
    for i in range(len(l)):
        heapq.heappush(heap, l[i])
    while len(heap) != 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost += a + b
        heapq.heappush(heap, a + b)
    print(cost)


if __name__ == "__main__":
    main()
