n = int(input())
al = list(map(int, input().split()))

vis = [0] * n
vis[0] = 1
crt = 0

st = ed = -1
while 1:
    nxt = al[crt] - 1
    if vis[nxt]:
        st = nxt
        ed = crt
        break
    vis[nxt] = 1
    crt = nxt

ans = []
while 1:
    a = al[st] - 1
    ans.append(a + 1)
    st = a
    if a == ed:
        break
ans.append(al[st])
print(len(ans))
print(*ans)
