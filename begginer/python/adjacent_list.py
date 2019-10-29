def main():
    number_of_v, edge = [int(i) for i in input().split()]
    adj_list = [[] for i in range(number_of_v)]
    for i in range(edge):
        s,e = [int(i) for i in input().split()]
        adj_list[s].append(e)
    print(adj_list)


if __name__ == "__main__":
    main()
