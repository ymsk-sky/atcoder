n = int(input())
s = input()
ans = -1
def check(i, cnt):
    res = False
    if i < n:
        res = s[i] == "-"
    if i - cnt - 1 >= 0:
        if s[i - cnt - 1] == "-":
            res = True
    return res
i = 0
while i < n:
    cnt = 0
    while i < n:
        if s[i] == "o":
            cnt += 1
        else:
            break
        i += 1
    if cnt > 0:
        if check(i, cnt):
            ans = max(ans, cnt)
    i += 1
print(ans)
