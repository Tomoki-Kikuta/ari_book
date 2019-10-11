def cal_min(page, contant, dicts):
    fro = 0
    to = 0
    num = 0
    candidate = {}
    answer = page
    while True:
        while to < page and num < len(dicts):
            if not candidate.get(contant[to]):
                candidate[contant[to]] = 1
                num += 1
            else:
                candidate[contant[to]] += 1
            to += 1

        if num < len(dicts):
            #froからtoまでのページでは全てのidを読むことができない
            break

        answer = min(answer, to - fro)

        candidate[contant[fro]] -= 1
        if candidate[contant[fro]] == 0:
            num -= 1
        fro += 1
        #範囲を狭くする
    return answer

def main():
    page = int(input())
    contant = [int(i) for i in input().split()]
    dicts = {}
    for i in range(page):
        if  not dicts.get(contant[i]):
            dicts[contant[i]] = 0
    answer = cal_min(page, contant, dicts)
    print(answer) 

if __name__ == "__main__":
    main()
