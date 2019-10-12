def quantifying(sta, N):
    status = []
    for i in range(N):
        #前を向いているなら0、向いてないならば1
        if sta[i] == "F":
            status.append(0)
        else:
            status.append(1)
    return status

def check(status, reverse, su, k, N):
    for i in range(N - k + 1, N):
        if i - k >= 0:
            su -= reverse[i - k]
        if (status[i] + su) % 2 != 0:
            return False
    return True

def main():
    N = int(input())
    sta = input()
    status = quantifying(sta, N) #状態の数値化
    min_operation = 5000
    min_k = N
    for k in range(1, N+1):
        su = 0 #reverseの和
        operation = 0 #何回反転させたか
        reverse = [0 for i in range(N)] #反転させたかどうか
        now = 0
        while now + k - 1  < N:
            if now - k >= 0:
                #now - k の区間が存在する
                su -= reverse[now - k]

            if (status[now] + su) % 2 != 0:
                #先頭の牛が後ろを向いている
                operation += 1
                reverse[now] = 1
            su += reverse[now]
            now += 1
        # print(reverse)
        if check(status, reverse, su, k, N):
            #残りの牛が前を向いているかチェック
            if min_operation > operation:
                min_operation = operation
                min_k = k

    print(min_k)
    print(min_operation)

if __name__ == "__main__":
    main()