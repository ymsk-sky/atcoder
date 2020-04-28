n=int(input())
s=input()
print(len([a for a,b in zip(s,s[1:]) if not a==b])+1)
