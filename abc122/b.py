s=input()
a=0
n=0
for c in s:
    if c in 'ACGT':
        n+=1
    else:
        n=0
    a=max(a,n)
print(a)
