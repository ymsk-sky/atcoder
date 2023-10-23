n = int(input())
s = input()

l = [0] * 10
for c in s:
    l[int(c)] += 1

cnt = 0
for i in range(3162278):
    t = str(i*i).zfill(n)
    m = [0] * 10
    for c in t:
        m[int(c)] += 1
    if l == m:
        cnt += 1
    if len(t) > n:
        break
print(cnt)
