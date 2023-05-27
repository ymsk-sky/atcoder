n = int(input())
s = input()
t = input()
for i in range(n):
    if s[i] == t[i]:
        continue
    if (s[i] in "l1") and (t[i] in "l1"):
        continue
    if (s[i] in "o0") and (t[i] in "o0"):
        continue
    print("No")
    exit()
print("Yes")
