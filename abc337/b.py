s = input()
a = b = c = 1
for ch in s[1:]:
    if ch == "A":
        if a == 0:
            print("No")
            exit()
    elif ch == "B":
        if b == 0:
            print("No")
            exit()
        a = 0
    elif ch == "C":
        if c == 0:
            print("No")
            exit()
        a = b = 0
print("Yes")
