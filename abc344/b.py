al = []
while 1:
    a = int(input())
    al.append(a)
    if a == 0:
        break
print(*al[::-1], sep="\n")
