h, w = map(int, input().split())
sl = [input() for _ in range(h)]

top = h - 1
bottom = 0
left = w - 1
right = 0
for i in range(h):
    for j in range(w):
        if sl[i][j] == "#":
            top = min(top, i)
            bottom = max(bottom, i)
            left = min(left, j)
            right = max(right, j)

for i in range(top, bottom + 1):
    for j in range(left, right + 1):
        if sl[i][j] == ".":
            print("No")
            exit()
print("Yes")
