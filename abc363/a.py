r = int(input())
for i in range(1, 1000):
    if r + i in (1, 100, 200, 300):
        print(i)
        break
