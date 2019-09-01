MAX_WEIGHT = 1000000000
def main():
    N = int(input())
    weight = [int(i) for i in input().split()]
    value  = [int(i) for i in input().split()]
    print_value = 0
    W = int(input())
    dp = [[MAX_WEIGHT for i in range(10001)] for j in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(10001):
            if value[i] <= j:
                dp[i+1][j] = min(dp[i][j], dp[i][j - value[i]] + weight[i])
            else:
                dp[i+1][j] = dp[i][j]
    for i in range(10001):
        if(dp[N][i] <= W):
            print_value = i
    print(print_value)

if __name__ == "__main__":
    main();