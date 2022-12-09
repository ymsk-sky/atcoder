n = int(input())
al = list(map(int, input().split()))
al.sort()
a = al[-1]

b = -1
for tmp in al[:-1]:
    dif = a - tmp
    if b < dif:
        b = tmp
print(a, b)