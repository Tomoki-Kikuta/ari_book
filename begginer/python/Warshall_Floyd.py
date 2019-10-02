INF = 1 << 21

def main():
    v, e = map(int, input().split())
    d = [[INF for i in range(v)] for j in range(v)]
    d[0][0] = 0
    for cost in range(e):
        fro, to, cost = map(int, input().split())
        d[fro][to] = cost
    for k in range(v):
        for i in range(v):
            for j in range(v):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])    
 
if __name__ == "__main__":
    main()