def init_union_find(v, parent, rank):
    for i in range(v):
        parent.append(i)
        rank.append(0)

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
    elif rank[to] > rank[fro]:
        parent[fro] = parent[to]
    else:
        parent[fro] = parent[to]
        rank[to] += 1
    return parent, rank

def kruskal_algorithm(v, s, adj_list):
    adj_list.sort()
    parent = []
    rank = []
    init_union_find(v, parent, rank)
    ans = 0
    for i in range(len(adj_list)):
            cost, fro, to = adj_list[i]
            if not same(fro, to, parent):
                unite(fro, to, parent, rank)
                ans += cost
    return ans

def main():
    v, e = map(int,input().split())
    s = 0
    adj_list = []
    for i in range(e):
        fro, to, cost = map(int,input().split())
        adj_list.append((cost, fro, to))
    # print(adj_list)
    ans = kruskal_algorithm(v, s, adj_list)
    print(ans)

if __name__ == "__main__":
    main()