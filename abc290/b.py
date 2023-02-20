n, k = map(int, input().split())
s = input()
ans = []
cnt = 0
for i in range(n):
    c = s[i]
    if c == "x":
        ans.append("x")
    else:
        if cnt < k:
            cnt += 1
            ans.append("o")
        else:
            ans.append("x")
print(*ans, sep="")
