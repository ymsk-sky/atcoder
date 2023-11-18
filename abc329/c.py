n = int(input())
s = input()
d = {chr(i + 97): 0 for i in range(26)}
bef = ""
cnt = 0
for c in s:
    if c == bef:
        cnt += 1
    else:
        if bef != "":
            d[bef] = max(d[bef], cnt)
        bef = c
        cnt = 1
d[c] = max(d[c], cnt)

ans = sum(d.values())
print(ans)
