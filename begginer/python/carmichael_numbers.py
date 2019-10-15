def mod_pow(x, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            print(n)
            res = res * x % mod
        x = x * x % mod
        n >>= 1
    return res


def main():
    n = int(input())
    for x in range(2, n):
        res = mod_pow(x, n, n)
        if x != res:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
