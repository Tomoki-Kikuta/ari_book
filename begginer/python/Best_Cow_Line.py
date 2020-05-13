def main():
    n = int(input())
    s = input()
    left = 0
    right = n - 1
    ans = str()
    while right >= left:
        if s[right] > s[left]:
            ans += s[left]
            left += 1
        else:
            ans += s[right]
            right -= 1
    print(ans)


if __name__ == "__main__":
    main()
