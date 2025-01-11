n = int(input())
al = list(map(int, input().split()))

left = 0
right = n + 1
while right - left > 1:
    mid = (left + right) // 2
    # mid個作成可能か
    cnt = 0
    j = n // 2
    for i in range(n // 2):
        a = al[i]
        while j < n:
            b = al[j]
            if a*2 <= b:
                cnt += 1
                j += 1
                break
            j += 1
    if cnt >= mid:
        left = mid
    else:
        right = mid
print(left)
