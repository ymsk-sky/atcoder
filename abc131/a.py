s=input()
for i,j in zip(s,s[1:]):
    if i==j:
        print('Bad')
        exit()
print('Good')
