from bisect import bisect_right, bisect_left

def search_r(t, i):
    ix = bisect_right(t, i)
    """bisect_right
    ソートされたリスト t へ i を挿入する位置(インデックス)を求める。
    すでに i が存在する場合、その右側(後ろ)のインデックスを返す。
    """
    return t[ix-1] == i

# search_r()と同じ動作
def search_l(t, i):
    ix = bisect_left(t, i)
    return t[ix] == i

""" リストt内に値iが含まれるかを検索する """
t = sorted([7, 5, 3, 1, 9])
i = 7
print(search_r(t, i))
print(search_l(t, i))
