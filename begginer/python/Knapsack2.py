def main():
    n = int(input())
    weight = []
    value = []
    for i in range(n):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    W = int(input())
    dp = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if weight[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
    print(dp[n][W])


if __name__ == "__main__":
    main()
