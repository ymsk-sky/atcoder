sl = input().split()
a = b = c = 0
if sl[0] == "<":
    b += 1
else:
    a += 1

if sl[1] == "<":
    c += 1
else:
    a += 1

if sl[2] == "<":
    c += 1
else:
    b += 1

if a == 1:
    print("A")
elif b == 1:
    print("B")
else:
    print("C")
