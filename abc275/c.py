s = [input() for _ in range(9)]
ans = set()
for i1 in range(1, 10):
    for j1 in range(1, 10):
        for i2 in range(1, 10):
            for j2 in range(1, 10):
                if i1 == i2 and j1 == j2:
                    continue
                if s[i1 - 1][j1 - 1] == "#" and s[i2 - 1][j2 - 1] == "#":
                    i3 = (i1 + i2 + j1 - j2) / 2
                    i4 = (i1 + i2 - j1 + j2) / 2
                    if i3 != int(i3) or i4 != int(i4):
                        continue
                    if (i3 <= 0 or i3 > 9) or (i4 <= 0 or i4 > 9):
                        continue
                    i3 = int(i3); i4 = int(i4)
                    j3 = (-i1 + i2 + j1 + j2) / 2
                    j4 = (i1 - i2 + j1 + j2) / 2
                    if j3 != int(j3) or j4 != int(j4):
                        continue
                    if (j3 <= 0 or j3 > 9) or (j4 <= 0 or j4 > 9):
                        continue
                    j3 = int(j3); j4 = int(j4)
                    if s[i3 - 1][j3 - 1] == "#" and s[i4 - 1][j4 - 1] == "#":
                        # ans += 1
                        ans.add(tuple(sorted([(i1, j1), (i2, j2), (i3, j3), (i4, j4)])))
print(len(ans))

"""
##.......
##.......
.........
.......#.
.....#...
........#
......#..
.........
.........

"""
