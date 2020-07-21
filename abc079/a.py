n=input()
print('Yes'if len(set(n[1:]))==1 or len(set(n[:-1]))==1 else'No')
