s=input()
t=input()
print(len([1 for a,b in zip(s,t) if a==b]))
