INF = 100000000

class Edge():
    def __init__(self, fro, to, cost):
        self.fro = fro
        self.to = to
        self.cost = cost

def cal_path(v, e, edge):
    d = []
    for i in range(v):
        d.append(INF)
    d[0] = 0

    update = True
    while update:
        update = False
        for i in range(e):
            fro = edge[i].fro
            to = edge[i].to
            cost = edge[i].cost
            if d[fro] != INF and d[to] > d[fro] + cost:
                d[to] = d[fro] + cost
                update = True
    return d

def main():
    v, e = map(int, input().split())
    edge= []
    for i in range(e):
        a = [int(i) for i in input().split()]
        edge.append(Edge(a[0], a[1], a[2]))

    d = cal_path(v, e, edge)

    for i in range(v):
        print(d[i])

if __name__ == "__main__":
    main()