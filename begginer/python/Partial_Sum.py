import sys


def main():
    n = int(input())
    number = [int(i) for i in input().split()]
    k = int(input())
    for i in range(1 << n):
        count = 0
        for j in range(n):
            if i >> j & 1:
                count += number[j]
        if count == k:
            print("Yes")
            sys.exit()
    print("No")


if __name__ == "__main__":
    main()
