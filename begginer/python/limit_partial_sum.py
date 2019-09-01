MAX_K = 100000
def main():
    N = int(input())
    number = [int(i) for i in input().split()]
    number_count = [int(i) for i in input().split()]
    K = int(input())
    dp = [-1 for i in range(MAX_K+1)]
    dp[0] = 0
    for i in range(N):
        for j in range(K+1):
            if dp[j] >= 0:
                dp[j] = number_count[i]
            elif j < number[i] or dp[j - number[i]] <= 0:
                dp[j] = -1
            else:
                dp[j] = dp[j - number[i]] - 1
    if dp[K] >= 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()