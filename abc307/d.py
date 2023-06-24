from collections import deque

n = int(input())
s = input()

ans = []
bef = 0  # いくつの"("に入っているか
tmp = deque()
crt = deque()
for i in range(n):
    c = s[i]
    if c == "(":
        if bef == 0:
            crt.append(c)
        else:
            tmp.append(crt.copy())
            crt.clear()
            crt.append(c)
        bef += 1
    elif c == ")":
        if bef == 0:
            ans.append(c)
        else:
            bef -= 1
            if bef == 0:
                crt = deque()
            else:
                crt = tmp.pop()
    else:
        # 文字
        if bef == 0:
            ans.append(c)
        else:
            crt.append(c)

while tmp:
    ans.append("".join(tmp.popleft()))
while crt:
    ans.append(crt.popleft())
print(*ans, sep="")
