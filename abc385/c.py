n = int(input())
hl = list(map(int, input().split()))

fin = [set() for _ in range(n)]
ans = 1
for i in range(n):
    h = hl[i]
    for width in range(1, n):
        if i + width >= n:
            break
        if width in fin[i]:
            continue
        tmp = 1
        for j in range(i + width, n, width):
            if hl[j] == h:
                fin[j].add(width)
                tmp += 1
            else:
                break
        ans = max(ans, tmp)
print(ans)
