s=input()
c=0
for n,r in zip(s[:len(s)//2],s[::-1]):
    if not n==r:
        c+=1
print(c)
