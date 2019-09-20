def main():
    N,M = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    MOD = int(input())
    dp = [[0 for i in range(N+1)] for j in range(M+1)]
    for i in range(N+1):
        dp[i][0] = 1
    for i in range(1,N+1):
        for j in range(1,M+1):
            if j - A[i-1] - 1 >= 0:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-A[i-1]-1]) % MOD
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD
    print(dp[-1][-1])

if __name__ == "__main__":
    main()