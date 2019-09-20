import heapq

def main():
    N = int(input())
    L = [int(i) for i in input().split()]
    cost = 0
    plate = []
    for i in range(N):
        heapq.heappush(plate,L[i])
    while len(plate) != 1:
        left = heapq.heappop(plate)
        right = heapq.heappop(plate)
        cost += left + right
        heapq.heappush(plate, left+right)

    print(cost)

if __name__ == "__main__":
    main()