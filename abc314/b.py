n = int(input())
l = []
for _ in range(n):
    c = int(input())
    al = set(list(map(int, input().split())))
    l.append(al)
x = int(input())
cnt = float("inf")
for al in l:
    if x in al:
        cnt = min(cnt, len(al))
ans = []
for i in range(n):
    if x in l[i] and len(l[i]) == cnt:
        ans.append(i + 1)
print(len(ans))
print(*ans)
