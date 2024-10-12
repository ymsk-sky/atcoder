n = int(input())
al = [input() for _ in range(n)]
bl = [["x"] * n for _ in range(n)]

for x in range(n // 2):
    for i in (x, n - x - 1):
        for j in range(x, n - x):
            if x % 4 == 0:
                u = n - j - 1
                v = i
            elif x % 4 == 1:
                u = n - i - 1
                v = n - j - 1
            elif x % 4 == 2:
                u = j
                v = n - i - 1
            else:
                u = i
                v = j
            bl[i][j] = al[u][v]
    for j in (x, n - x - 1):
        for i in range(x, n - x):
            if x % 4 == 0:
                u = n - j - 1
                v = i
            elif x % 4 == 1:
                u = n - i - 1
                v = n - j - 1
            elif x % 4 == 2:
                u = j
                v = n - i - 1
            else:
                u = i
                v = j
            bl[i][j] = al[u][v]
for b in bl:
    print("".join(b))


"""
4
..##
##..
....
####

i=1,2
"""
