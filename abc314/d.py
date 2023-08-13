n = int(input())
s = input()
q = int(input())
ll = [input().split() for _ in range(q)]
u = [None] * n
toUpper = toLower = False
for l in ll[::-1]:
    t, x, c = int(l[0]), int(l[1]), l[2]
    if t == 1:
        # x文字目をcに変更
        if not u[x - 1]:
            if toLower:
                c = c.lower()
            elif toUpper:
                c = c.upper()
            u[x - 1] = c
    elif t == 2:
        # 大文字を小文字に変更
        if toLower or toUpper:
            continue
        toLower = True
    elif t == 3:
        # 小文字を大文字に変更
        if toLower or toUpper:
            continue
        toUpper = True
ans = []
for i in range(n):
    if u[i]:
        ans.append(u[i])
    else:
        if toLower:
            ans.append(s[i].lower())
        elif toUpper:
            ans.append(s[i].upper())
        else:
            ans.append(s[i])
print(*ans, sep="")
