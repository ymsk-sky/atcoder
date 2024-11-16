from itertools import groupby

n, k = map(int, input().split())
s = input()
l = [(c, len(list(v))) for c, v in groupby(s)]
cnt = 0
ans = []
for c, v in l:
    if c == "1":
        cnt += 1
        if cnt == k:
            bef = ans.pop()
            ans.append(c * v)
            ans.append(bef)
        else:
            ans.append(c * v)
    else:
        ans.append(c * v)
print("".join(ans))
