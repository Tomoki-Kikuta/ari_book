import bisect


def main():
    N, W = map(int, input().split())
    value = [0] * N
    weight = [0] * N
    for i in range(N):
        v, w = map(int, input().split())
        value[i] = v
        weight[i] = w
    half = N // 2
    vw_from_0_to_half = []
    for i in range(1 << half):
        v = 0
        w = 0
        for j in range(half):
            if (i >> j) & 1:
                v += value[j]
                w += weight[j]
        vw_from_0_to_half.append([w, v])
    vw_from_0_to_half.sort()
    max_ = 0
    for i in range(len(vw_from_0_to_half)):
        max_ = max(max_, vw_from_0_to_half[i][1])
        vw_from_0_to_half[i][1] = max_

    ans = 0
    for i in range(1 << (N - half)):
        v = 0
        w = 0
        for j in range(N - half):
            if (i >> j) & 1:
                v += value[j + half]
                w += weight[j + half]
        if w <= W:
            a = bisect.bisect_right(vw_from_0_to_half, [W - w, 10**17])
            b = vw_from_0_to_half[a - 1][1]
            ans = max(ans, b + v)
    print(ans)


if __name__ == '__main__':
    main()
