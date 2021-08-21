from itertools import permutations
s,k=map(str,input().split())
k=int(k)
l=list(set(list(permutations(s))))
l.sort()
print(''.join(list(l[k-1])))
