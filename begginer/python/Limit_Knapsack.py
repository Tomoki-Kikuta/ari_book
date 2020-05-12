def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    m = [int(i) for i in input().split()]
    K = int(input())
    dp = [-1] * (K+1)
    dp[0] = 0
    for i in range(n):
        for j in range(K+1):
            if dp[j] >= 0:
                dp[j] = m[i]
            elif a[i] < j and dp[j - a[i]] <= 0:
                dp[j] = -1
            else:
                dp[j] = dp[j - a[i]] - 1 
    if dp[K] != -1:
        print("Yes")
    else:
        print("No")
 
if __name__ == "__main__":
    main()
