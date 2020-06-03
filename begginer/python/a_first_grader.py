import numpy as np


def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    dp = np.zeros((N - 1, 21))
    dp[0][A[0]] = 1
    for i in range(1, N - 1):
        num = A[i]
        for j in range(21):
            c = dp[i - 1][j]
            if c > 0:
                plus = num + j
                if plus <= 20:
                    dp[i][plus] += c
                minus = j - num
                if minus >= 0:
                    dp[i][minus] += c
    ans = dp[-1][A[N - 1]]
    print(int(ans))


if __name__ == '__main__':
    main()
