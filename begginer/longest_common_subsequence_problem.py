def main():
    q = int(input())
    for _ in range(q):
        X = input()
        Y = input()
        x = len(X)
        y = len(Y)
        dp = [[0 for b in range(y + 1)] for a in range(x + 1)]
        for i in range(1, x+1):
            for j in range(1, y+1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp[-1][-1])


if __name__ == '__main__':
    main()
