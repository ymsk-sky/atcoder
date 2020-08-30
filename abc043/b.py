s=''
for c in input():
    if c=='B':
        if s!='':
            s=s[:-1]
    else:
        s+=c
print(s)
