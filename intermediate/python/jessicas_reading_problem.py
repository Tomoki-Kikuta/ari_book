def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    book_id = {}
    for i in range(N):
        if book_id.get(a[i]) is None:
            book_id[a[i]] = 1
        else:
            book_id[a[i]] += 1
    left = 0
    right = 0
    count = {}
    num = 0
    res = N
    while True:
        while right < N and num != len(book_id):
            if count.get(a[right]) is None or count[a[right]] == 0:
                count[a[right]] = 1
                num += 1
            else:
                count[a[right]] += 1
            right += 1
        if num != len(book_id):
            break
        res = min(res, right - left)
        count[a[left]] -= 1
        if count[a[left]] == 0:
            num -= 1
        left += 1
    print(res)


if __name__ == '__main__':
    main()
