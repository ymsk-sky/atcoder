a, b, c, d = map(int, input().split())

l = [[2, 1, 0, 1], [1, 2, 1, 0]]

x = c - a  # x長さ
i1 = a % 4
i_num = [0] * 4
for i in range(4):
    i_num[(i + i1) % 4] = x//4 + int(x%4 > i)

y = d - b  # y長さ
j1 = b % 2
j_num = [0] * 2
for j in range(2):
    j_num[(j + j1) % 2] = y//2 + int(y%2 > j)

ans = 0
for i in range(4):
    for j in range(2):
        ans += l[j][i] * i_num[i] * j_num[j]
print(ans)


"""
-10**9<=a,b,c,d<=10**9
a<c かつ b<d

1 2 1 0
2 1 0 1
のパターン
"""