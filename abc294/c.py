n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = [(al[i], i) for i in range(n)] + [(bl[j], j + n) for j in range(m)]
cl.sort()

ans_a = [0] * n
ans_b = [0] * m
for k in range(n + m):
    _, i = cl[k]
    if i < n:
        ans_a[i] = k + 1
    else:
        ans_b[i - n] = k + 1

print(*ans_a)
print(*ans_b)
