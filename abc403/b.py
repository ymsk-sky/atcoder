t = input()
u = input()

n = len(t)
m = len(u)
for i in range(n - m + 1):
    x = 0
    for j in range(m):
        c = t[i + j]
        d = u[j]
        if c != "?" and c != d:
            break
    else:
        print("Yes")
        exit()
print("No")
