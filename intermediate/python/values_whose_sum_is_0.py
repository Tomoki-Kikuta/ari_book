import bisect


def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    D = [int(i) for i in input().split()]
    AB = []
    CD = []
    for i in range(N):
        for j in range(N):
            AB.append(A[i] + B[j])
            CD.append(C[i] + D[j])
    AB.sort()
    CD.sort()

    ans = 0
    for i in range(len(AB)):
        now = AB[i]
        ans += bisect.bisect_right(CD,  - 1 * now) - bisect.bisect_left(CD, -1 * now)
    print(ans)


if __name__ == '__main__':
    main()
