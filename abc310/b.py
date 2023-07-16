n, m = map(int, input().split())
pl = []
fll = []
for _ in range(n):
    p, c, *fl = map(int, input().split())
    pl.append(p)
    fll.append(set(fl))

def hasall(i, j):
    return len(fll[i] - fll[j]) == 0

def plus(i, j):
    return len(fll[j] - fll[i]) > 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        cnt = 0
        if pl[i] >= pl[j]:
            cnt += 1
        if hasall(i, j):
            cnt += 1
        if pl[i] > pl[j] or plus(i, j):
            cnt += 1
        if cnt == 3:
            print("Yes")
            exit()
print("No")
