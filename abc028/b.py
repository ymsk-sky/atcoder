d={c:0for c in 'ABCDEF'}
for c in input():
    d[c]+=1
print(' '.join([str(c)for c in d.values()]))
