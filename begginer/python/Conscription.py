STANDARD = 10000

def init_union_find(v, parent, rank):
    for i in range(v):
        parent.append(i)
        rank.append(0)
    return parent, rank

def get_parent(u, parent):
    if parent[u] == u:
        return parent[u]
    else:
        parent[u] = get_parent(parent[u], parent)
        return parent[u]

def same(fro, to, parent):
    a = get_parent(fro, parent)
    b = get_parent(to, parent)
    if a == b:
        return True
    else:
        return False

def unite(fro, to, parent, rank):
    if rank[fro] > rank[to]:
        parent[to] = parent[fro]
    elif rank[fro] < rank[to]:
        parent[fro] = parent[to]
    else:
        parent[fro] = parent[to]
        rank[to] += 1
    return parent, rank

def cal_cost(adj_list, v, edge):
    min_cost = STANDARD * v
    parent = []
    rank = []
    init_union_find(v, parent, rank)
    for i in range(edge):
        cost, fro, to = adj_list[i]
        if not same(fro, to, parent):
            unite(fro, to, parent, rank)
            min_cost += cost
    return min_cost

def main():
    N, M, R = map(int, input().split())
    adj_list = []
    for i in range(R):
        x, y, d = map(int, input().split())
        adj_list.append((-1 * d, x, y+N))
    adj_list.sort()
    min_cost = cal_cost(adj_list, N+M, R)
    print(min_cost)


if __name__ == "__main__":
    main()