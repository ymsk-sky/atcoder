n = int(input())
sl = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        t = sl[i] + sl[j]
        if t == t[::-1]:
            print("Yes")
            exit()

print("No")
