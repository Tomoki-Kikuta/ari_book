def main():
    size = int(input())
    S = int(input())
    array = [int(i) for i in input().split()]
    left = 0
    right = 1
    count = 2
    answer = size
    array_sum = array[left] + array[right]
    while True:
        if array_sum < S:
            #解ではないので、範囲を広げる
            right += 1
            count += 1
            if right == size:
                #範囲をこえたらブレイク
                break
            array_sum += array[right]
        else:
            #解の候補であるので、範囲を狭める
            answer = min(count, answer)
            left += 1            
            count -= 1
            array_sum -= array[left - 1] #leftの左隣は要素ではない

    if count == size + 1:
        #解が存在しないとき
        answer = 0
    print(answer)

if __name__ == "__main__":
    main()