b = int(input())
for a in range(1, 18):
    if a**a == b:
        print(a)
        exit()
print(-1)
