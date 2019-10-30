INF = 10 ** 6


def make_d(town, road):
    d = [[INF for i in range(town)] for j in range(town)]
    for i in range(road):
        s, t, distance = map(int, input().split())
        s -= 1
        t -= 1
        d[s][t] = distance
        d[t][s] = distance
    return d


def cal_min_time(coach_ticket, town, road, start, goal, d, head):
    dp = []
    # dpの初期化(かかる時間をINFとする)
    for i in range(1 << coach_ticket):
        dp.append([])
        for j in range(town):
            dp[i].append(INF)
    # 全てのチケットが残っていて、スタートの街にいるとき、時間を0とする
    dp[(1 << coach_ticket) - 1][start] = 0

    res = INF
    for S in range((1 << coach_ticket) - 1, -1, -1): 
        res = min(res, dp[S][goal])
        for i in range(town):
            #　iの都市にいて、残っている乗車券の集合がSである
            for j in range(coach_ticket):
                if S >> j & 1:
                    # j番目の乗車券が残っている時
                    for u in range(town):
                        # 乗車券jを使ってuに行く
                        if d[i][u] >= 0:
                            dp[S & ~(1 << j)][u] = min(dp[S & ~(1 << j)][u], dp[S][i] + d[i][u] / head[j])

    return res


def main():
    while True:
        coach_ticket, town, road, start, goal = map(int, input().split())
        if coach_ticket == town == road == start == goal == 0:
            break
        start -= 1
        goal -= 1
        head = [int(i) for i in input().split()]

        d = make_d(town, road)

        ans = cal_min_time(
              coach_ticket, town, road, start, goal, d, head)
        if ans > 100 * 30:
            print("impossible")
        else:
            print("{:.3f}".format((round(ans, 3))))


if __name__ == "__main__":
    main()
