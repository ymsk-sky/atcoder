s=[c for c in input()]
t=[c for c in input()]
s.sort()
t.sort(reverse=True)
s=''.join(s)
t=''.join(t)
print('Yes'if s<t else'No')
