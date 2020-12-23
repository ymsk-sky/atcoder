h,w=map(int,input().split())
s=[input() for _ in range(h)]
ans=0
for y in range(h):
    for x in range(w):
        s[y][x]
print(ans)
"""
4 6
#..#..
.....#
....#.
#.#...
横
022022
555550
444401
010333
縦
043021
243320
243302
040312
-> 0でなければ横+縦-1
"""
