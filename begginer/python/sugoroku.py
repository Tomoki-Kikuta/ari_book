def euclid(a, b, x, y):
    d = a
    if b == 0:
        x = 1
        y = 0
        return d, y, x
    else:
        d, x, y = euclid(b, a % b, y, x)
        y += int(a / b) * x
        return d, y, x

def main():
    a, b = map(int, input().split())
    flag = True
    if a < b:
        a, b = b, a
        flag = False
    gcd, x, y = euclid(a, b, 0, 0)
    if gcd != 1:
        print(-1)
    else:
        if flag:
            print("{} {} {} {}".format(y, 0, 0, x))
        else:
            print("{} {} {} {}".format(0, y, x, 0))

if __name__ == "__main__":
    main()