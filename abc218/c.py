n=int(input())
s=[input() for _ in range(n)]
t=[input() for _ in range(n)]
def minimaze(grid):
    for u in range(n):
        if '#' in grid[u]:
            break
    for d in range(n-1,-1,-1):
        if '#' in grid[d]:
            break
    for l in range(n):
        column=[row[l] for row in grid[u:d+1]]
        if '#' in column:
            break
    for r in range(n-1,-1,-1):
        column=[row[r] for row in grid[u:d+1]]
        if '#' in column:
            break
    minimazed = [row[l:r+1] for row in grid[u:d+1]]
    return minimazed
def rotate(grid):
    rotated=list(zip(*grid[::-1]))
    return rotated
s=minimaze(s)
t=minimaze(t)
t=rotate(t)
for _ in range(4):
    s=rotate(s)
    if s==t:
        print('Yes')
        exit()
print('No')
