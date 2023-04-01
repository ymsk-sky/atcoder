from bisect import bisect_left

n, x = map(int, input().split())
al = list(map(int, input().split()))
al.sort()

for a in al:
    i = bisect_left(al, a - x)
    for p in (i - 1, i, i + 1):
        if 0 > p or p >= n:
            continue
        b = al[p]
        if a - b == x:
            print("Yes")
            exit()
print("No")
