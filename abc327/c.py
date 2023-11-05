al = [list(map(int, input().split())) for _ in range(9)]
for i in range(9):
    if len(set(al[i])) != 9 or len(set([al[j][i] for j in range(9)])) != 9:
        print("No")
        exit()
    if i%3 == 0:
        l = []
        for j in range(9):
            l.append(al[i][j])
            l.append(al[i + 1][j])
            l.append(al[i + 2][j])
            if j%3 == 2:
                if len(set(l)) != 9:
                    print("No")
                    exit()
                l.clear()
print("Yes")
