n = int(input())
s = input()
for i in range(1, n):
    l = 0
    for k in range(n - i):
        if s[k] != s[k + i]:
            l = k + 1
        else:
            break
    print(l)
