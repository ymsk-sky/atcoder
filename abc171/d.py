n=int(input())  # alの個数
nums=[0]*10**5
for i in list(map(int,input().split())):
    nums[i-1]+=1
q=int(input())  # 操作回数
bcs=[list(map(int,input().split())) for _ in range(q)]  # q個の操作： bをcへ変換
sum_=sum([i*v for i,v in enumerate(nums,start=1)])
for b,c in bcs:
    sum_+=(c-b)*nums[b-1]
    nums[c-1]+=nums[b-1]
    nums[b-1]=0
    print(sum_)
