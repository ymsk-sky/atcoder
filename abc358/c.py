n, m = map(int, input().split())
sl = [input() for _ in range(n)]
ans = n
for state in range(1 << n):
    l = [0] * m
    for i in range(n):
        if (state >> i) & 1:
            for j in range(m):
                if sl[i][j] == "o":
                    l[j] = 1
    if sum(l) == m:
        ans = min(ans, state.bit_count())
print(ans)
