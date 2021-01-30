a,b,c=map(int,input().split())
if c==0:
    print('Aoki' if b>=a else 'Takahashi')
else:
    print('Takahashi' if a>=b else 'Aoki')
