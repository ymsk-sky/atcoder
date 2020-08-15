s=input()
r='R'
if s[0]==r and s[1]==r:
    if s[1]==s[2]:
        print(3)
    else:
        print(2)
elif s[1]==r and s[2]==r:
    print(2)
elif s[0]==r or s[1]==r or s[2]==r:
    print(1)
else:
    print(0)
