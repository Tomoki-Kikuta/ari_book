def main():
    N = int(input())
    prime = []
    is_prime = [True for i in range(N+1)]
    is_prime[0] = is_prime[1] = False
    for i in range(2, N+1):
        if is_prime[i]:
            # iは素数である
            prime.append(i)
            for j in range(2 * i, N+1, i):
                # iの倍数は素数でない
                is_prime[j] = False
    # N以下の素数を表示
    print(prime)


if __name__ == "__main__":
    main()
