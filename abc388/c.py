from bisect import bisect_left

n = int(input())
al = list(map(int, input().split()))

ans = 0
for a in al:
    i = bisect_left(al, 2*a)
    ans += n - i
print(ans)
