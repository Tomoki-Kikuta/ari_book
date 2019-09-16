def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    dp = [0] * N
    ans = 0
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        ans = max(ans, dp[i])
    print(ans)

if __name__ == "__main__":
    main()