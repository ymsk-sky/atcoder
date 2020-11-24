"""いもす試行
先頭==末尾の範囲ではだめそう
"""
n=int(input())
imosu=[0]*(10**7)
for v in range(1,10):
    imosu[v]+=1
    imosu[v+1]-=1
    s=str(v)
    for x in range(1,5):
        start_pos=int(s+'0'*x+s)
        end_pos=int(s+'9'*x+s)
        imosu[start_pos]+=1
        imosu[end_pos+1]-=1
for v in range(10,n+1):
    if v%10==0:
        continue
    s=str(v)
    head=s[0]
    tail=s[-1]
    if head==tail:
        val=int(head)
        imosu[val]+=1
        imosu[val+1]-=1
    for x in range(0,5):
        start_pos=int(tail + '0'*x + head)
        end_pos=int(tail + '9'*x + head)
        imosu[start_pos]+=1
        imosu[end_pos+1]-=1
for i in range(10**7-1):
    imosu[i+1]+=imosu[i]
print(sum(imosu[:n+1]))
