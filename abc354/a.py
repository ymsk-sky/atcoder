h = int(input())
x = 0
for i in range(0, 100):
    x += 2**i
    if x > h:
        break
print(i + 1)
