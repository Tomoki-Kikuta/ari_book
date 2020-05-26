import sys
from collections import deque
import copy
def main():
    N = int(input())
    M = int(input())
    dp = [[0 for i in range(M)] for j in range(N)]
    ans_dp = copy.deepcopy(dp)
    ans = N * M + 1
    for i in range(M):
        dp[i] = [int(k) for k in input().split()]

    count = 0
    for i in range(1 << N): 
        copy_dp = copy.copy(dp)
        where_ = [[0 for i in range(M)] for j in range(N)]
        for j in range(N):
            if i >> j & 1:
                count += 1
                where_[0][j] = 1
                copy_dp[0][j] = (copy_dp[0][j] + 1) % 2
                copy_dp[1][j] = (copy_dp[1][j] + 1) % 2
                if j - 1 >= 0:
                    copy_dp[1][j - 1] = (copy_dp[1][j - 1] + 1) % 2
                if j + 1 > N:
                    copy_dp[0][j + 1] = (copy_dp[0][j + 1] + 1) % 2
        for x in range(1, M-1):
            for y in range(N):
                if copy_dp[x - 1][y] == 1:
                    count += 1
                    where_[x][y] = 1
                    copy_dp[x - 1][y] = 0
                    copy_dp[x][y] = (copy_dp[x][y] + 1) % 2
                    copy_dp[x + 1][y] = (copy_dp[x + 1][y] + 1) % 2
                    if y - 1 >= 0:
                        copy_dp[x][y - 1] = (copy_dp[x][y - 1] + 1) % 2
                    if y + 1 < N:
                        copy_dp[x][y + 1] = (copy_dp[x][y + 1] + 1) % 2
        flag = True
        for y in range(N):
            if copy_dp[M - 1][y] == 1:
                flag = False
                break
        if flag:
            if count < ans:
                ans = count
                ans_dp = copy.copy(where_)

    if ans == N * M + 1:
        print('IMPOSSIBLE')
    else:
        for i in range(M):
            for j in range(N):
                print(ans_dp[i][j], end=' ')
            print()


if __name__ == '__main__':
    main()
