n = int(input())
b = bin(n)
m = len(b)
for i in range(m):
    if b[m - i - 1] != "0":
        break
print(i)
