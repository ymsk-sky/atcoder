a, b = map(int, input().split())
edges = [[], [2], [1, 3], [2], [5], [4, 6], [5], [8], [7, 9], [8]]
if b in edges[a]:
    print("Yes")
else:
    print("No")
