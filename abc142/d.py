a,b=map(int,input().split())
def factorization(n):
    arr=[]
    temp=n
    for i in range(2,int(-(-n**0.5//1))+1):
        if temp%i==0:
            #cnt=0
            while temp%i==0:
                #cnt+=1
                temp//=i
            arr.append(i)
    if temp!=1:
        arr.append(temp)
    if arr==[]:
        arr.append(n)
    return arr
fa=factorization(a)
fb=factorization(b)
s=set(fa)&set(fb)
#print(fa,fb,s)
if 1 in s:
    print(1)
    exit()
print(len(s)+1)
