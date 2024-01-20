n = int(input())
al = list(map(int, input().split()))
l = [0] * n
for a in al:
    if a == -1:
        continue
    l[a - 1] = 1
i = l.index(0) + 1
ans = []
while i != -1:
    ans.append(i)
    i = al[i - 1]
print(*ans[::-1])

"""
6
4 1 -1 5 3 2
1 2  3 4 5 6
[1, 1, 1, 1, 1, 0]
[6, 2, 1, 4, 5, 3]
"""