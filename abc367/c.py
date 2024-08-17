n, k = map(int, input().split())
rl = list(map(int, input().split()))
ans = []
def f(i: int, l: list):
    for x in range(1, rl[i] + 1):
        l.append(x)
        if i == n - 1:
            if sum(l) % k == 0:
                ans.append(l.copy())
        else:
            f(i + 1, l)
        l.pop()
f(0, [])
for an in sorted(ans):
    print(*an)
