def make_combination(fro, to, value, weight, W):
    """ビット演算が重い"""
    combination = []
    for i in range(1 << (to - fro)):
        w = 0
        v = 0
        for j in range(to - fro):
            if i >> j & 1:
                w += weight[j + fro]
                v += value[j + fro]
                if w > W:
                    break
        if w > W:
            continue
        combination.append([w, v])

    # 必要のない組み合わせを弾く
    combination.sort()
    for i in range(len(combination) - 1):
        if combination[i][1] > combination[i + 1][1]:
            combination[i + 1][1] = combination[i][1]

    return combination


def cal_ans(from_0_to_harf_combination, from_harf_to_N_combination, W):
    ans = 0

    """ 尺取り法 """
    left = 0
    right = len(from_harf_to_N_combination) - 1
    for left in range(len(from_0_to_harf_combination)):
        now_weight = from_0_to_harf_combination[left][0]
        now_value = from_0_to_harf_combination[left][1]
        while now_weight + from_harf_to_N_combination[right][0] > W:
            right -= 1
            if right < 0:
                right = 0
                break
        if now_weight + from_harf_to_N_combination[right][0] <= W:
            ans = max(ans, now_value + from_harf_to_N_combination[right][1])

    """ 二分探索 """
    # for now in range(len(from_0_to_harf_combination)):
    #     now_weight = from_0_to_harf_combination[now][0]
    #     now_value = from_0_to_harf_combination[now][1]
    #     count = 0
    #     left = 0
    #     right = len(from_0_to_harf_combination) - 1
    #     while count < 45:
    #         mid = (left + right) // 2
    #         if now_weight + from_harf_to_N_combination[mid][0] > W:
    #             right = mid - 1
    #         else:
    #             ans = max(ans, now_value + from_harf_to_N_combination[mid][1])
    #             left = mid + 1
    #         count += 1

    return ans


def main():
    N, W = map(int, input().split())
    harf = N // 2
    value = []
    weight = []
    for i in range(N):
        v, w = map(int, input().split())
        value.append(v)
        weight.append(w)

    # 半分全列挙の組み合わせを前半と後半で作る
    from_0_to_harf_combination = make_combination(0, harf, value, weight, W)
    from_harf_to_N_combination = make_combination(harf, N, value, weight, W)

    # 尺取り法か二分探索で計算
    ans = cal_ans(from_0_to_harf_combination, from_harf_to_N_combination, W)
    print(ans)


if __name__ == "__main__":
    main()
