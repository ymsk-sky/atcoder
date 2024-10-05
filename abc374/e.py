n, x = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

left = 0
right = 10**16
while right - left > 1:
    mid = (left + right) // 2  # = 製造能力W
    # mid個がx円で達成可能か?
    s = 0
    # 各工程でmidを達成できる最低価格をそれぞれ算出
    for a, p, b, q in l:
        # 機械S(A個をP円)のほうをベースに考える
        base = -(-mid // a)  # base個導入
        res = base * p  # 費用
        cnt = base * a # mid以上製品を作れる
        for k in range(1, min(20001, base + 1)):
            # k個分を取り換える
            tmp = (base - k) * p
            lack = max(0, mid - (cnt - k*a))  # 不足個数
            # 不足分をもう一方で埋める
            tmp += -(-lack // b) * q
            res = min(res, tmp)
        # 機械T(B個をQ円)のほうをベースに考える
        base = -(-mid // b)  # base個導入
        res = min(res, base * q)
        cnt = base * b # mid以上製品を作れる
        for k in range(1, min(20001, base + 1)):
            # k個分を取り換える
            tmp = (base - k) * q
            lack = max(0, mid - (cnt - k*b))  # 不足個数
            # 不足分をもう一方で埋める
            tmp += -(-lack // a) * p
            res = min(res, tmp)
        s += res
    if s <= x:
        # 可能
        left = mid
    else:
        # 不可能
        right = mid
print(left)
