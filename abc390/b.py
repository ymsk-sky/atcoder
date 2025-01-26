n = int(input())
al = list(map(int, input().split()))

a, b = al[0], al[1]
for c, d in zip(al[1:], al[2:]):
    if b*c != a*d:
        print("No")
        exit()
print("Yes")
