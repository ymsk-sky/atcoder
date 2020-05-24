s=input()
u,l=int(s[:2]),int(s[2:])
if 1<=u<=12:
    if 1<=l<=12:
        print('AMBIGUOUS')
        exit()
    else:
        print('MMYY')
        exit()
if 1<=l<=12:
    print('YYMM')
    exit()
print('NA')
