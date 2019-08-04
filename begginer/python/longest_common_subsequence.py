def cal_partial_string(N, M, s, t):
    dp = [[0 for i in range(M+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(M):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    return dp[N][M]

def main():
    N = int(input())
    M = int(input())
    s = input()
    t = input()
    longest_partial_sum = cal_partial_string(N, M, s, t)
    print(longest_partial_sum)

if __name__ == "__main__":
    main()