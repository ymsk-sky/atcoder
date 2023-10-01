n, m = map(int, input().split())
s = input()
t = input()
a = s == t[:n]
b = s == t[m - n:]
if a and b:
    print(0)
elif a:
    print(1)
elif b:
    print(2)
else:
    print(3)
