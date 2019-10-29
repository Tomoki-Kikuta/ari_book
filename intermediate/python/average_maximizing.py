W_V_MAX = 1000000

def cheak(value, weight, x, size, choose_num):
    ans = []
    res = 0
    for i in range(size):
        ans.append(value[i] - x * weight[i])
    ans.sort(reverse=True)
    for i in range(choose_num):
        res += ans[i]
    if res >= 0:
        return True
    else:
        return False

def main():
    size = int(input())
    choose_num = int(input())
    wv = [int(i) for i in input().split()]
    weight = []
    value = []
    for i in range(len(wv)):
        if i % 2 == 0:
            weight.append(wv[i])
        else:
            value.append(wv[i])
    left = 0
    right = W_V_MAX
    for i in range(100):
        mid = (left + right) / 2
        if cheak(value, weight, mid, size,choose_num):
            #解である可能性があり、midが大きい場合が解の可能性がある
            left = mid
        else:
            #解ではなく、midを小さくする必要がある
            right = mid

    print((left + right) / 2)

if __name__ == "__main__":
    main()