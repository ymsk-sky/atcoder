from bisect import bisect_right, bisect_left

n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
al.sort()
bl.sort()

left = 0
right = 10**9 + 1
while right - left > 1:
    mid = (left + right)//2
    i = bisect_right(al, mid)
    j = m - bisect_left(bl, mid)
    if i >= j:
        right = mid
    else:
        left = mid
print(right)
