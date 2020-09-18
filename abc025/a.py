s=input()
n=int(input())
l=[]
for c in s:
    for d in s:
        l.append(c+d)
print(l[n-1])
