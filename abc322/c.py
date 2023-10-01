from bisect import bisect_left

n, m = map(int, input().split())
al = list(map(int, input().split()))

for i in range(1, n + 1):
    x = bisect_left(al, i)
    print(al[x] - i)
