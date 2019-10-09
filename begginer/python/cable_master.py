import math

def cheak(array, size, k, mid):
    count = 0
    for i in range(size):
        count += int(array[i] / mid)

    if count >= k:
        return True
    else:
        return False

def main():
    size = int(input())
    k = int(input())
    array = [float(i) for i in input().split()]
    right = 100000
    left = 1
    for i in range(100):
        mid = (left + right) / 2
        if cheak(array, size, k, mid):
            left = mid
        else:
            right = mid

    print("{}".format(math.floor(right * 100) / 100))

if __name__ == "__main__":
    main()