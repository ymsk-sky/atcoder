from itertools import groupby

n, k = map(int, input().split())
s = input()
l = [(x, len(list(v))) for x, v in groupby(s)]
ans = 0
for x, v in l:
    if x == "O":
        ans += v // k
print(ans)
