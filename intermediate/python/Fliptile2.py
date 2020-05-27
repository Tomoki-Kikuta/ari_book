import sys
from collections import deque
import copy
import numpy as np


def main():
    N = int(input())
    M = int(input())
    dp = np.zeros((M + 2, N + 2))
    for i in range(1, M+1):
        input_line = [int(k) for k in input().split()]
        for j in range(1, N+1):
            dp[i][j] = input_line[j - 1]
    ans_dp = copy.deepcopy(dp)
    ans = N * M + 1
    for i in range(1 << N): 
        count = 0
        copy_dp = copy.copy(dp)
        where_ = [[0 for i in range(M+2)] for j in range(N+2)]
        for j in range(N):
            if i >> j & 1:
                count += 1
                where_[0][j] = 1
                copy_dp[0][j] = not copy_dp[0][j]
                copy_dp[1][j] = not copy_dp[1][j]
                copy_dp[1][j - 1] = not copy_dp[1][j - 1]
                copy_dp[0][j + 1] = not copy_dp[0][j + 1]
        for x in range(1, M):
            for y in range(1, N+1):
                if copy_dp[x - 1][y] == 1:
                    count += 1
                    where_[x][y] = 1
                    copy_dp[x - 1][y] = 0
                    copy_dp[x][y] = not copy_dp[x][y]
                    copy_dp[x + 1][y] = not copy_dp[x + 1][y]
                    if y - 1 >= 0:
                        copy_dp[x][y - 1] = not copy_dp[x][y - 1]
                    if y + 1 < N:
                        copy_dp[x][y + 1] = not copy_dp[x][y + 1]
        flag = True
        for y in range(N):
            if copy_dp[M][y] == 1:
                flag = False
                break
        if flag:
            if count < ans:
                ans = count
                ans_dp = copy.copy(where_)

    if ans == N * M + 1:
        print('IMPOSSIBLE')
    else:
        for i in range(1, M+1):
            for j in range(1, N+1):
                print(ans_dp[i][j], end=' ')
            print()


if __name__ == '__main__':
    main()
