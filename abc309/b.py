n = int(input())
al = [list(input()) for _ in range(n)]
bl = []
for i in range(n):
    if i == 0:
        bl.append([al[i + 1][0]] + al[i][:n - 1])
    elif i == n - 1:
        bl.append(al[i][1:] + [al[i - 1][n - 1]])
    else:
        bl.append([al[i + 1][0]] + al[i][1:n - 1] + [al[i - 1][n - 1]])

for b in bl:
    print(*b, sep="")
