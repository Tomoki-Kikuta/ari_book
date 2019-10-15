import sys

def mod_pow(x, n, mod):
    if n == 1:
        return x
    res = mod_pow(x * x, int(n / 2), mod)
    return res

def main():
    n = int(input())
    for x in range(2, n):
        xn = mod_pow(x, n, n)
        xn_mod_n = 0
        if n % 2 == 1:
            xn_mod_n = (xn * x) % n
        else:
            xn_mod_n %= n
        print("{} {}".format(xn_mod_n,x))
        if x != xn_mod_n:
            print("No")
            exit()

    print("Yes")

if __name__ == "__main__":
    main()