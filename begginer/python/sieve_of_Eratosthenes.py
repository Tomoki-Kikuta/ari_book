def main():
    N = int(input())
    prime = []
    is_prime = [True for i in range(N+1)]
    is_prime[0] = is_prime[1] = False
    for i in range(2,N+1):
        if is_prime[i] == True:
            prime.append(i)
            for j in range(2 * i, N+1, i):
                is_prime[j] = False
    print(prime)

if __name__ == "__main__":
    main()