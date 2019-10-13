import copy
"""反転させる順番が関係ないときは、自分で解が一意に定まるように操作する
   pythonの関数はリストも参照渡しのため注意が必要"""


def print_ans(height, width, ans, flip):
    if ans == -1:
        # 解がない
        print("IMPOSSIBLE")
    else:
        for i in range(height):
            for j in range(width):
                print(flip[i][j], end=" ")
            print()


def change_tile(height, width, tile, h, w):
    tile[h][w] += 1  # 今のタイルを反転させる
    if h - 1 >= 0:
        tile[h-1][w] += 1  # 上のタイルを反転させる
    if h + 1 < height:
        tile[h + 1][w] += 1  # 下のタイルを反転させる
    if w - 1 >= 0:
        tile[h][w - 1] += 1  # 左のタイルを反転させる
    if w + 1 < width:
        tile[h][w + 1] += 1  # 右のタイルを反転させる
    return tile


def cal_num(height, width, flip):
    num = 0
    for h in range(height):
        for w in range(width):
            num += flip[h][w]
    return num


def cal_fliptile(height, width, tile, flip):
    for h in range(1, height):
        for w in range(width):
            if tile[h-1][w] % 2 == 1:
                flip[h][w] = 1
                tile = change_tile(height, width, tile, h, w)

    # 全て白であるかチェック
    for w in range(width):
        if tile[height - 1][w] % 2 == 1:
            # 黒のタイルがある
            return -1, flip

    # 反転したタイルの数
    num = cal_num(height, width, flip)
    return num, flip


def change_tile_0(height, width, tile, flip, w):
    if w < width:
        # 値渡しにするための処理
        tile1 = copy.deepcopy(tile)
        flip1 = copy.deepcopy(flip)
        tile2 = copy.deepcopy(tile)
        flip2 = copy.deepcopy(flip)

        num1, flip1 = change_tile_0(height, width, tile1, flip1, w+1)

        flip2[0][w] = 1
        tile2 = change_tile(height, width, tile2, 0, w)
        num2, flip2 = change_tile_0(height, width, tile2, flip2, w+1)

        # 解が存在するとき小さい方を返す
        if num1 < 0 and num2 < 0:
            return num2, flip2
        elif num1 > 0 and num2 < 0:
            return num1, flip1
        elif num1 < 0 and num2 > 0:
            return num2, flip2
        else:
            if num1 < num2:
                return num1, flip1
            else:
                return num2, flip2

    else:
        # １行目が決まったとき
        copy_flip = copy.deepcopy(flip)
        copy_tile = copy.deepcopy(tile)
        num, copy_flip = cal_fliptile(height, width, copy_tile, copy_flip)
        return num, copy_flip


def main():
    # 入力と初期化
    height = int(input())
    width = int(input())
    tile = [[] for j in range(height)]
    flip = [[0 for i in range(width)] for j in range(height)]
    for i in range(height):
        tile[i] = [int(i) for i in input().split()]

    num, flip = change_tile_0(height, width, tile, flip, 0)
    print_ans(height, width, num, flip)


if __name__ == "__main__":
    main()
