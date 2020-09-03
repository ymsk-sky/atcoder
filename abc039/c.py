s=input()
r=['Do','Re','Mi','Fa','So','La','Si']
l=['WBWBWWBWBWBWWBWBWWBW',
   'WBWWBWBWBWWBWBWWBWBW',
   'WWBWBWBWWBWBWWBWBWBW',
   'WBWBWBWWBWBWWBWBWBWW',
   'WBWBWWBWBWWBWBWBWWBW',
   'WBWWBWBWWBWBWBWWBWBW',
   'WWBWBWWBWBWBWWBWBWWB']
for p,q in zip(l,r):
    if s==p:
        print(q)
        exit()
