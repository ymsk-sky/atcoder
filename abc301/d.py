s = input()
n = int(input())
l = len(s)

ans = []
for i in range(l):
    c = s[i]
    if c == "?":
        tmp = "".join(ans) + "1" + "".join([x if x != "?" else "0" for x in s[i+1:]])
        tmp = int(tmp, 2)
        if tmp > n:
            ans.append("0")
        else:
            ans.append("1")
    else:
        ans.append(c)

ans = int("".join(ans), 2)
print(-1 if ans > n else ans)
