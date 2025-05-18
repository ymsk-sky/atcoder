a, b, c, d = map(int, input().split())

s = f"{a:02d}{b:02d}"
t = f"{c:02d}{d:02d}"
print("Yes" if s > t else "No")
