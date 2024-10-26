sl = [input() for _ in range(8)]
h = set()
w = set()
for i in range(8):
    for j in range(8):
        if sl[i][j] == "#":
            h.add(i)
            w.add(j)

ans = (8 - len(h)) * (8 - len(w))
print(ans)
