from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
al = list(map(int, input().split()))
al.sort()
ans = []
for _ in range(q):
    b, k = map(int, input().split())
    left = -1
    right = 10**9
    while right - left > 1:
        mid = (left + right) // 2
        il = bisect_left(al, b - mid)
        ir = bisect_right(al, b + mid)
        cnt = ir - il
        if cnt >= k:
            right = mid
        else:
            left = mid
    ans.append(right)
print(*ans, sep="\n")


"""
1<=n,q<=10**5
-10**8<=a,b<=10**8
1<=k<=n

10 1
-84 -60 -41 -100 8 -8 -52 -62 -61 -76
-52 5

"""
