n, k = map(int, input().split())
al = list(map(int, input().split()))

left = 0
right = 10**9 + 1
while right - left > 1:
    mid = (left + right)//2
    num = 0
    for a in al:
        num += -(-a // mid) - 1
    if num > k:
        # 不可
        left = mid
    else:
        # 可
        right = mid
print(right)