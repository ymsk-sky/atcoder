from collections import Counter

def No():
    print("No")
    exit()

s = input()
n = len(s)
if n % 2 == 1:
    No()

for i in range(n//2):
    if s[2*i] != s[2*i + 1]:
        No()

c = Counter(s)
for v in c.values():
    if v != 2:
        No()

print("Yes")
