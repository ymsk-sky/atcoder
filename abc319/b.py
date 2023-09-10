n = int(input())
s = []
for i in range(n + 1):
    for j in range(1, 10):
        if n%j != 0:
            continue
        if i%(n//j) == 0:
            s.append(j)
            break
    else:
        s.append("-")
print(*s, sep="")
