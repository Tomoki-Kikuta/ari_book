def main():
    n, m = map(int, input().split())
    c = [int(i) for i in input().split()]
    dp = [[10 ** 5 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m+1):
        dp[i][0] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if c[i - 1] <= j:
                dp[i][j] = min(dp[i][j - c[i - 1]] + 1, dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
