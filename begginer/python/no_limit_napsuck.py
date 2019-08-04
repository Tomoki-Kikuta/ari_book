def cal_value(N, weight, value, limit_weight):
    dp = [[0 for i in range(limit_weight+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(limit_weight+1):
            if weight[i] <= j:
                dp[i+1][j] = max(dp[i+1][j-weight[i]]+value[i],dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]
    return dp[N][limit_weight]

def main():
    N = int(input())
    weight = list()
    value = list()
    for i in range(N):
        w,v = [int(i) for i in input().split()]
        weight.append(w)
        value.append(v)
    limit_weight = int(input())
    max_value = cal_value(N, weight, value, limit_weight)
    print(max_value)

if __name__ == "__main__":
    main()