def f(st, ed):
    x = ed - st + 1
    return x * (x - 1) // 2

n = int(input())
al = list(map(int, input().split()))
if n == 1:
    print(1)
    exit()
ans = n
st = 0
for i, (a1, a2) in enumerate(zip(al, al[1:])):
    if st == i:
        dif = a2 - a1
    else:
        if a2 - a1 == dif:
            continue
        else:
            ans += f(st, i)
            st = i
            dif = a2 - a1
ans += f(st, i + 1)
print(ans)
