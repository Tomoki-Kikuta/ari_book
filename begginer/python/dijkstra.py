import heapq
INF = 1<<21

def make_adj_list(v):
    adj_list = []
    for i in range(v):
        adj_list.append([])
    return adj_list

class Edge():
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost    

def dijkstra(v, e, adj_list, s):
    heap = []
    d = []
    path = []
    for i in range(v):
        d.append(INF)
    d[0] = 0
    heapq.heappush(heap, (0, s))
    while len(heap) != 0:
        candidate_d, now_v = heapq.heappop(heap)
        if d[now_v] < candidate_d:
            continue
        path.append(now_v)
        #経路を保存しておく
        for v in adj_list[now_v]:
            if d[v.to] > d[now_v] + v.cost:
                d[v.to] = d[now_v] + v.cost
                heapq.heappush(heap,(d[v.to], v.to))
    return d, path

def main():
    v, e = map(int, input().split())
    adj_list = make_adj_list(v)
    for i in range(e):
        a = [int(i) for i in input().split()]
        adj_list[a[0]].append(Edge(a[1], a[2]))
        adj_list[a[1]].append(Edge(a[0], a[2]))
        
    d, path = dijkstra(v, e, adj_list, 0)

    for i in range(v):
        print("{} {}".format(path[i], d[path[i]]))

if __name__ == "__main__":
    main()