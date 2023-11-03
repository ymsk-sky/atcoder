from bisect import bisect_left

n, m = map(int, input().split())
al = list(map(int, input().split()))
al.sort()
ans = 0
for i in range(n):
    a = al[i]
    j = bisect_left(al, a + m)
    ans = max(ans, j - i)
print(ans)


"""
8 6
2 3 5 7 11 13 17 19

i=0
j=8
"""