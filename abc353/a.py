n = int(input())
hl = list(map(int, input().split()))
h1 = hl[0]
for i in range(1, n):
    if hl[i] > h1:
        print(i + 1)
        exit()
print(-1)
