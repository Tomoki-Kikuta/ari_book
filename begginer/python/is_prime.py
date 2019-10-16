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
    if is_prime(N):
        print("素数である")
    else:
        print("素数でない")


if __name__ == "__main__":
    main()