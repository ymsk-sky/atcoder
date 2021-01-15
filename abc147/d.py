def main():
    n=int(input())
    l=list(map(int,input().split()))
    mod=10**9+7
    ans=0
    for d in range(60):
        b0=0
        for a in l:
            b=a>>d&1
            if b==0:
                b0+=1
        ans+=b0*(n-b0)*2**d
        ans%=mod
    print(ans)
if __name__=='__main__':
    main()
"""
3
1 2 3
1XOR2 + 1XOR3 + 2XOR3
01|10 + 01|11 + 10|11

10
3 1 4 1 5 9 2 6 5 3
"""
