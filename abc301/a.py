n = int(input())
s = input()
t = s.count("T")
a = s.count("A")
if t == a:
    if s[-1] == "T":
        print("A")
    else:
        print("T")
elif t > a:
    print("T")
else:
    print("A")
