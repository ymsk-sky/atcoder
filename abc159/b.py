s=input()
n=len(s)
r=s[::-1]
if s==r and s[:(n-1)//2]==s[:(n-1)//2][::-1] and r[:(n-1)//2]==r[:(n-1)//2][::-1]:
    print("Yes")
else:
    print("No")
