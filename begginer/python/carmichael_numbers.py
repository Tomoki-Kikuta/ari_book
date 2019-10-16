def mod_pow(x, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n >>= 1
    return res


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def main():
    n = int(input())

    if is_prime(n):
        # nが素数であるとき
        print("No")
        exit()

    for x in range(2, n):
        res = mod_pow(x, n, n)
        if x != res % n:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
