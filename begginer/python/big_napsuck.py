def cal_array_w_v_pair(w_v_pair, hight, now_weight, now_value,
                       limit, return_array):
    # pythonの配列は参照渡しであるので、return_arrayに加えることで値が追加される
    if hight < limit:
        cal_array_w_v_pair(w_v_pair, hight + 1, now_weight, now_value,
                           limit, return_array)
        now_weight += w_v_pair[hight][0]
        now_value += w_v_pair[hight][1]
        cal_array_w_v_pair(w_v_pair, hight + 1, now_weight, now_value,
                           limit, return_array)
    else:
        return_array.append((now_weight, now_value))


def cal_max_value(front_w_v_pair, back_w_v_pair, limit_weight):
    max_value = 0
    left = 0
    right = len(back_w_v_pair) - 1
    while right >= 0 and left < len(front_w_v_pair):
        now_weight = front_w_v_pair[left][0] + back_w_v_pair[right][0]
        now_value = front_w_v_pair[left][1] + back_w_v_pair[right][1]
        if now_weight <= limit_weight:
            # weightの合計がlimit_weight以下の時、weightを大きくできる、解の候補でもある
            max_value = max(max_value, now_value)
            left += 1
        else:
            # weightの合計がlimit_weightより大きい時、weightは小さくしなければならない
            right -= 1

    return max_value


def check(array):
    increase_array = []
    max_value = -1
    for i in range(len(array)):
        if max_value < array[i][1]:
            # weightが増えた時価値が上がる場合
            max_value = array[i][1]
            increase_array.append(array[i])
    return increase_array


def main():
    N = int(input())
    weight = [int(i) for i in input().split()]
    value = [int(i) for i in input().split()]
    limit_weight = int(input())
    w_v_pair = []
    front_w_v_pair = []
    back_w_v_pair = []
    half = int(N / 2)
    for i in range(N):
        w_v_pair.append((weight[i], value[i]))

    # 半分全列挙を使ってそれぞれの組み合わせをだしておく
    cal_array_w_v_pair(w_v_pair, 0, 0, 0, half, front_w_v_pair)
    cal_array_w_v_pair(w_v_pair, half, 0, 0, N, back_w_v_pair)

    # 尺取り法を用いるためsortしておく
    front_w_v_pair.sort()
    back_w_v_pair.sort()

    # weightが増えたときに、価値が上がらないと尺取り法は使えないので、そのような組み合わせを弾く
    increase_front_w_v_pair = check(front_w_v_pair)
    increase_back_w_v_pair = check(back_w_v_pair)

    max_value = cal_max_value(increase_front_w_v_pair,
                              increase_back_w_v_pair, limit_weight)

    print(max_value)


if __name__ == "__main__":
    main()
