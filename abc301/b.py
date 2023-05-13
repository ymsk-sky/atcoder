n = int(input())
al = list(map(int, input().split()))
ans = []
for a, b in zip(al, al[1:]):
    if a > b:
        l = list(range(a - 1, b, -1))
    else:
        l = list(range(a + 1, b))
    ans.extend([a] + l)
ans.append(b)
print(*ans)
