s = input()
t = []
for i in range(1, len(s)//2 + 1):
    t.append(s[2*i - 1])
    t.append(s[2*i - 2])
print(*t, sep="")
