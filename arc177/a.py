l = list(map(int, input().split()))
n = int(input())
xl = list(map(int, input().split()))
xl.sort(reverse=True)
c = [1, 5, 10, 50, 100, 500]
for x in xl:
    for i in range(5, -1, -1):
        if l[i] * c[i] <= x:
            x -= l[i]*c[i]
            l[i] = 0
        else:
            m = x // c[i]
            x %= c[i]
            l[i] -= m
    if x != 0:
        print("No")
        exit()
print("Yes")
