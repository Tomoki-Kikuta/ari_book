import math

def cheak(array, n, cow, d):
    last = 0
    for i in range(1,cow):
        crt = last + 1
        while crt < n and array[crt] - array[last] < d:
            crt += 1
        if crt == n:
            return False
        last = crt
    return True
        
def main():
    n = int(input())
    cow = int(input())
    array = [int(i) for i in input().split()]
    array.sort()
    right = 1000000000
    left = 0
    while right - left > 1:
        mid = (left + right) / 2
        if cheak(array, n, cow, mid):
            left = mid
        else:
            right = mid

    print(int(right))

if __name__ == "__main__":
    main()