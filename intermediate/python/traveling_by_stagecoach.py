INF = 10 ** 12


def make_adj_list(town, road):
    adj_list = [[INF for i in range(town)] for j in range(town)]
    for i in range(road):
        s, t, distance = map(int, input().split())
        adj_list[s][t] = distance
        adj_list[t][s] = distance
    return adj_list


def main():
    while True:
        coach_ticket, town, road, start, goal = map(int, input().split())
        if coach_ticket == town == road == start == goal == 0:
            break
        head = [int(i) for i in input().split()]
        adj_list = make_adj_list(town, road)


if __name__ == "__main__":
    main()
