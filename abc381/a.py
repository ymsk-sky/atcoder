def No():
    print("No")
    exit()

n = int(input())
s = input()

if n % 2 == 0:
    No()
if s.count("/") != 1:
    No()

a, b = s.split("/")
if "2" in a or "1" in b:
    No()

if len(a) != len(b):
    No()

print("Yes")
