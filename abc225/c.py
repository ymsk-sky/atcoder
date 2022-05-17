N, M = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(N)]

j0 = B[0][0] % 7
if j0 == 0 or j0 > 7:
    print("No")
    exit()
i0 = int((B[0][0] - j0) / 7 + 1)

for i, row in enumerate(B):
    for j, v in enumerate(row):
        if v == (i0 + i - 1) * 7 + (j0 + j):
            pass
        else:
            print("No")
            exit()
print("Yes")
