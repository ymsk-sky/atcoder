t=int(input())  # t秒以内
n=int(input())  # たこ焼き数
al=list(map(int,input().split()))  # たこやき完成時間列
m=int(input())  # 客数
bl=list(map(int,input().split()))  # 来客時間列
for b in bl:
    l=[a for a in al if b-a<=t and b-a>=0]
    if len(l)==0:
        print('no')
        exit()
    c=min(l)
    al.remove(c)
print('yes')
