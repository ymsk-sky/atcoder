from collections import Counter

s = input()
t = input()
at = "atcoder"

c1 = Counter(s)
c2 = Counter(t)

a = 0
b = 0
for c in range(97, 123):
    c = chr(c)
    if c in at:
        if c in c1:
            if c in c2:
                if c1[c] > c2[c]:
                    a += c1[c] - c2[c]
                else:
                    b += c2[c] - c1[c]
            else:
                a += c1[c]
        elif c in c2:
            b += c2[c]
    else:
        if (c in c1) and (c in c2):
            if c1[c] != c2[c]:
                print("No")
                exit()
        elif (c in c1) or (c in c2):
            print("No")
            exit()

if c2["@"] >= a and c1["@"] >= b:
    print("Yes")
else:
    print("No")
