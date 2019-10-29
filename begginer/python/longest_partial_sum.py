def cal_partial_string(N, M, s, t):
    dp = [[0 for in range(M)] for in range(N)]

def main():
    N = int(input())
    M = int(input())
    s = input()
    t = input()
    longest_partial_sum = cal_partial_string(N, M, s, t)
    print(longest_partial_sum)

if __name__ == "__main__":
    main()