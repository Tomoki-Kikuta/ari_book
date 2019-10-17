def sum_list_A_B(N, A, B):
    # AとBの和をだしておく
    AB = {}
    for i in range(N):
        for j in range(N):
            if AB.get(A[i] + B[j]):
                AB[A[i] + B[j]] += 1
            else:
                AB[A[i] + B[j]] = 1
    return AB


def cal_four_list_sum(N, AB, C, D):
    count = 0
    for i in range(N):
        for j in range(N):
            if AB.get((C[i] + D[j]) * -1):
                # CとDの和に-1をかけたものが、AとBの和で存在する
                count += AB[(C[i] + D[j]) * -1]
    return count


def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    D = [int(i) for i in input().split()]
    AB = sum_list_A_B(N, A, B)
    count = cal_four_list_sum(N, AB, C, D)
    print(count)


if __name__ == "__main__":
    main()
