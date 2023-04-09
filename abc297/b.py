s = input()
b1 = s.find("B")
b2 = s.rfind("B")
if b1%2 == b2%2:
    print("No")
    exit()
r1 = s.find("R")
r2 = s.rfind("R")
k = s.find("K")
if r1 < k < r2:
    print("Yes")
else:
    print("No")

"""
K
Q
RR
BB
NN
"""
