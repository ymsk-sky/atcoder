s = input()
t = input()
n = len(s)
i = 0
j = 0
while i < n and j < 3:
    c = s[i].upper()
    d = t[j]
    if c == d:
        i += 1
        j += 1
    else:
        i += 1

if j == 3:
    print("Yes")
elif j == 2 and t[2] == "X":
    print("Yes")
else:
    print("No")
