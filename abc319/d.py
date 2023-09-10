n, m = map(int, input().split())
ll = list(map(int, input().split()))
left = 0
right = n * 10**10
while right - left > 1:
    mid = (left + right) // 2
    lines = 0  # 合計行数
    tmp = 0  # 今の行の長さ
    i = 0  # 確認中の単語
    while i < n:
        l = ll[i]
        if tmp == 0:
            if l > mid:
                lines = float("inf")
                break
            else:
                tmp += l
                i += 1
        else:
            if tmp + 1 + l > mid:
                lines += 1
                tmp = 0
            else:
                tmp += 1 + l
                i += 1
    if i == n and tmp > 0:
        lines += 1

    if lines > m:
        left = mid
    else:
        right = mid
print(right)
