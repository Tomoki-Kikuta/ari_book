import heapq

def heap_push(h, j, N, A, B, now_point):
    while j < N:
        if A[j] <= now_point:
            heapq.heappush(h, B[j])
            j += 1
        else:
            break
    return h, j, now_point

def main():
    N,L,P = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    B = [int(i) * -1 for i in input().split()]
    h = []
    j = 0
    count = 0
    now_point = 0
    heapq.heappush(h, P * -1)
    while(True):
        if len(h) > 0:
            now_point += heapq.heappop(h) * -1
            count += 1
            if now_point >= L:
                print(count - 1)
                break
            heap_push(h, j, N, A, B, now_point)
        else:
            print(-1)
            break

if __name__ == "__main__":
    main()