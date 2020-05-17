n=input()
if int(n[-1]) in [2,4,5,7,9]:
    print('hon')
    exit()
elif int(n[-1]) in [0,1,6,8]:
    print('pon')
    exit()
else:
    print('bon')
