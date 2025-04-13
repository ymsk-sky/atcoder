n = int(input())
ans = 0
state = 0
for _ in range(n):
    s = input()
    if s == "login":
        state = 1
    elif s == "logout":
        state = 0
    elif s == "public":
        pass
    elif s == "private":
        if state == 0:
            ans += 1
print(ans)
