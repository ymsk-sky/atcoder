s = input()
t = input()
if len(s) > len(t):
    print("No")
    exit()
if s in t:
    if t.index(s) == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")