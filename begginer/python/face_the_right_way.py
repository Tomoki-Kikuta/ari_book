def quantifying(sta, N):
    status = []
    for i in range(N):
        # 前を向いているなら0、向いてないならば1
        if sta[i] == "F":
            status.append(0)
        else:
            status.append(1)
    return status


def check(status, reverse, total, k, N):
    for i in range(N - k + 1, N):
        if i - k >= 0:
            total -= reverse[i - k]
        if (status[i] + total) % 2 != 0:
            return False
    return True


def main():
    N = int(input())
    sta = input()
    status = quantifying(sta, N)  # 状態の数値化

    min_operation = sum(status)
    min_k = 1

    for k in range(2, N+1):
        total = 0  # reverseの和
        operation = 0  # 何回反転させたか
        reverse = [0 for i in range(N)]  # 反転させたかどうか
        for now in range(N - k + 1):
            if now - k >= 0:
                # now - k の区間が存在する
                total -= reverse[now - k]

            if (status[now] + total) % 2 != 0:
                # 先頭の牛が後ろを向いている
                operation += 1
                reverse[now] = 1
            total += reverse[now]
            now += 1
        # print(reverse)
        if check(status, reverse, total, k, N):
            # 残りの牛が前を向いているかチェック
            if min_operation > operation:
                min_operation = operation
                min_k = k

    print(min_k)
    print(min_operation)


if __name__ == "__main__":
    main()
