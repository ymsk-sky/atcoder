n, a, b = map(int, input().split())
dl = list(map(int, input().split()))
w = a + b
dl = [d % w for d in dl]
l = max(dl) - min(dl) + 1
m = (min(dl) - max(dl) + 1) % w
print("Yes" if l <= a or m <= a else "No")
