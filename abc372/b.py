m = int(input())
l = []
while m > 0:
    for a in range(11):
        if 3**a > m:
            l.append(a - 1)
            m -= 3**(a - 1)
            break
    else:
        l.append(10)
        m -= 3**10
print(len(l))
print(*l)
