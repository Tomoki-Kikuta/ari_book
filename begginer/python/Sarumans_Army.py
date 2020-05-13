import sys


def main():
    n = int(input())
    r = int(input())
    x = [int(i) for i in input().split()]
    now = 0
    next_ = 0
    ans = 0
    while now < x[n - 1]:
        ans += 1
        while x[next_] - now < r:
            next_ += 1
            if next_ == n:
                break
        now = x[next_]   
    print(ans)


if __name__ == "__main__":
    main()
