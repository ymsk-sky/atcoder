o=input()
e=input()+' '
print((''.join(['{}{}'.format(a,b) for a,b in zip(o,e)])).replace(' ',''))
