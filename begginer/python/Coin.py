def main():
    C = [int(i) for i in input().split()]
    money = [1, 5, 10, 50, 100, 500]
    A = int(input())
    ans = 0
    for i in range(len(C) - 1, -1, -1):
        if A > money[i]:
            can_ = min(A // money[i], C[i])
            A -= can_ * money[i]
            ans += can_
    print(ans)


if __name__ == "__main__":
    main()
