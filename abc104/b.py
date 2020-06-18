s=input()
if s[0]=='A' and s[2:-1].count('C')==1:
    for i in range(len(s)):
        if not (i==0 or i==s[2:-1].index('C')+2):
            if not s[i].islower():
                print('WA')
                exit()
    print('AC')
    exit()
print('WA')
