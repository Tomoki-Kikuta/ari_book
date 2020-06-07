def cal_expo(m, n, MOD):
    if m == 1:
        return 1
    ans = 1
    while n != 1:
        if n % 2 != 0:
            ans = (ans * m) % MOD
        n //= 2
        m = (m ** 2) % MOD
    ans = (ans * m) % MOD
    return ans


def main():
    m, n = map(int, input().split())
    MOD = 10 ** 9 + 7
    ans = cal_expo(m, n, MOD)
    print(ans)


if __name__ == '__main__':
    main()
