n=int(input())
l=list(map(int,input().split()))
def k(a):
    if a%2==1:
        return 0
    return k(a/2)+1
print(sum([k(a) for a in l]))
