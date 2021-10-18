s=input()
l=[]
for _ in range(len(s)):
    s=s[1:]+s[0]
    l.append(s)
l.sort()
print(l[0])
print(l[-1])
