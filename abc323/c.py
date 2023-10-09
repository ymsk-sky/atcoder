n, m = map(int, input().split())
al = list(map(int, input().split()))
sl = [input() for _ in range(n)]

mx = [-1, -1]
for i in range(n):
    s = sl[i]
    point = sum([al[j] for j in range(m) if s[j] == "o"]) + (i + 1)
    if point > mx[0]:
        mx = [point, i]

ans = []
for i in range(n):
    if i == mx[1]:
        ans.append(0)
        continue
    point = i + 1
    rem = []
    s = sl[i]
    for j in range(m):
        if s[j] == "o":
            point += al[j]
        else:
            rem.append(al[j])
    rem.sort(reverse=True)
    cnt = 0
    for r in rem:
        cnt += 1
        point += r
        if point > mx[0]:
            break
    ans.append(cnt)
print(*ans, sep="\n")
