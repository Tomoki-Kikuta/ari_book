def is_prime(N):
    if N == 1:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

def main():
    N = int(input())
    is_prime(N)

if __name__ == "__main__":
    main()