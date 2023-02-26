n = int(input())
s = input()
x, y = 0, 0
vis = set([(x, y)])
for c in s:
    if c == "R":
        x += 1
    elif c == "L":
        x -= 1
    elif c == "U":
        y += 1
    else:
        y -= 1
    if (x, y) in vis:
        print("Yes")
        exit()
    vis.add((x, y))
print("No")
