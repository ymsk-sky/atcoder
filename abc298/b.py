n = int(input())
al = [list(map(int, input().split())) for _ in range(n)]
bl = [list(map(int, input().split())) for _ in range(n)]

for _ in range(4):
    al = [list(l) for l in zip(*al[::-1])]
    ng = 0
    for i in range(n):
        for j in range(n):
            if al[i][j] == 1:
                if bl[i][j] == 0:
                    ng = 1
    if not ng:
        print("Yes")
        break
else:
    print("No")
