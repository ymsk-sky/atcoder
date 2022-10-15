from bisect import bisect_left

n = int(input())
al = list(map(int, input().split()))

ks = [0] * n

l = sorted(list(set(al)))
ll = len(l)

for a in al:
    x = bisect_left(l, a)
    ks[ll - x - 1] += 1

for k in ks:
    print(k)

"""
6
2 7 1 8 2 8

2
1
2
1
0
0

1 2 7 8
"""