def main():
    n = int(input())
    s = [int(i) for i in input().split()]
    t = [int(i) for i in input().split()]
    to_from = []
    for i in range(n):
        to_from.append((t[i], s[i]))
    to_from.sort()
    now = 0
    ans = 0
    for i in range(n):
        if now < to_from[i][1]:
            now = to_from[i][0]
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
