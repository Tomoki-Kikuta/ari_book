import math

def main():
    size = int(input())
    array = [int(i) for i in input().split()]
    k = int(input())
    right = size - 1
    left = 0
    while right != left:
        mid = int((left + right) / 2)
        if array[mid] >= k:
            right = mid
            #kと等しい場合,解である可能性がある
        else:
            left = mid + 1
            #解である可能性はない,
        
    print(right)

if __name__ == "__main__":
    main()