from collections import deque 
import numpy as np
INF = 1 << 21

def bfs(start_x, start_y, goal_x, goal_y, maze):
    next_go = deque()
    next_go.append((start_x, start_y))
    while len(next_go) != 0:
        now_x, now_y = next_go.pop()
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x + y) % 2 != 0:
                    next_x = now_x + x
                    next_y = now_y + y
                    if maze[next_x][next_y] != -1 and maze[next_x][next_y] > maze[now_x][now_y]:
                        maze[next_x][next_y] = maze[now_x][now_y] + 1
                        next_go.append((next_x, next_y))

def main():
    n, m = map(int, input().split())
    maze = - np.ones((n+2, m+2))
    start_x = 0
    start_y = 0
    goal_x = 0
    goal_y = 0
    for i in range(n):
        line = input()
        for j in range(len(line)):
            if line[j] == 'S':
                start_x = i + 1
                start_y = j + 1
                maze[i + 1][j + 1] = 0
            elif line[j] == 'G':
                goal_x = i + 1
                goal_y = j + 1
                maze[i + 1][j + 1] = INF
            elif line[j] == '.':
                maze[i + 1][j + 1] = INF
    bfs(start_x, start_y, goal_x, goal_y, maze)
    print(maze[goal_x][goal_y])


if __name__ == "__main__":
    main()
