def init(N, parent, rank):
    for i in range(N):
        parent.append(i)
        rank.append(0)
    return parent, rank

def find(parent, v):
    if parent[v] == v:
        return v
    else:
        parent[v] = find(parent, parent[v])
        return parent[v]

def unite(parent, rank, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return 
    elif rank[a] < rank[b]:
        parent[a] = b
        return parent
    elif rank[a] > b:
        parent[b] = a
        return parent
    else:
        parent[b] = a
        rank[a] += 1
        return parent, rank

def union_find():
    N = int(input())
    x, y = [int(i) for i in input().split()]
    parent = []
    rank = []
    init(N, parent, rank)
    unite(parent, rank, x, y)

if __name__ == "__main__":
    union_find()