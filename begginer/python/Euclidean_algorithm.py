def gcd(a, b):
    if a % b == 0:
        return b
    else:
        ans = gcd(b, a % b)
        return ans

def main():
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    ans = gcd(a, b)
    print(ans)

if __name__ == "__main__":
    main()