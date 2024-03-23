w, b = map(int, input().split())
p = "wbwbwwbwbwbw" * 5*(w + b)
W, B = 0, 0
for i in range(w + b):
    if p[i] == "w":
        W += 1
    else:
        B += 1
for i in range(w + b, 4*(w + b)):
    if W == w and B == b:
        print("Yes")
        exit()
    if p[i - (w + b)] == "w":
        W -= 1
    else:
        B -= 1
    if p[i] == "w":
        W += 1
    else:
        B += 1
print("No")
