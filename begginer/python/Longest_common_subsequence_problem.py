def main():
    n = int(input())
    m = int(input())
    s = input()
    t = input()
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j] , dp[i][j - 1])
    print(dp[n][m])

if __name__ == "__main__":
    main()
