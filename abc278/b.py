h, m = map(int, input().split())
f = True
def is_ans(i, j):
    i = str(i).zfill(2)
    j = str(j).zfill(2)
    i, j = i[0] + j[0], i[1] + j[1]
    i = int(i)
    j = int(j)
    if 0 <= i <= 23 and 0 <= j <= 59:
        return True
    else:
        return False
for i in range(h, 24):
    if f:
        f = False
        for j in range(m, 60):
            if is_ans(i, j):
                print(i, j)
                exit()
    else:
        for j in range(60):
            if is_ans(i, j):
                print(i, j)
                exit()

for i in range(24):
    for j in range(60):
        if is_ans(i, j):
            print(i, j)
            exit()
