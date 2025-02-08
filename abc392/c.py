n = int(input())
pl = list(map(int, input().split()))
ql = list(map(int, input().split()))


ans = [0] * n
for i, q in enumerate(ql):
    ans[q - 1] = ql[pl[i] - 1]
print(*ans)
