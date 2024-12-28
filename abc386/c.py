k = int(input())
s = input()
t = input()

n = len(s)
m = len(t)
if n == m:
    cnt = 0
    for i in range(n):
        if s[i] != t[i]:
            cnt += 1
    print("Yes" if cnt <= 1 else "No")
elif n == m + 1:  # n>m
    for i in range(m):
        if s[i] != t[i]:
            break
    else:
        print("Yes")
        exit()
    for j in range(i, m):
        if s[j + 1] != t[j]:
            print("No")
            exit()
    print("Yes")
elif n + 1 == m:  # n<m
    for i in range(n):
        if s[i] != t[i]:
            break
    else:
        print("Yes")
        exit()
    for j in range(i, n):
        if s[j] != t[j + 1]:
            print("No")
            exit()
    print("Yes")
else:
    print("No")
