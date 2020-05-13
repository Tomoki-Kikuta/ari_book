from collections import deque


def lake_counting(now_x, now_y, n, m, garden):
    garden[now_x][now_y] = '.'
    next_go = deque()
    next_go.append((now_x, now_y))
    while len(next_go) != 0:
        now_x, now_y = next_go.pop() 
        for x in range(-1, 2):
            for y in range(-1, 2):
                if  x == 0 and y == 0:
                    continue
                next_x = now_x + x
                next_y = now_y + y
                if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m and garden[next_x][next_y] == 'W':
                    garden[next_x][next_y] = '.'
                    next_go.append((next_x, next_y))


def main():
    n, m = map(int, input().split())
    garden = []
    lake = 0
    for i in range(n):
        g = input()
        garden.append(list(g))
    for i in range(n):
        for j in range(m):
            if garden[i][j] == 'W':
                lake += 1
                lake_counting(i, j, n, m, garden)
    print(lake)


if __name__ == "__main__":
    main()
