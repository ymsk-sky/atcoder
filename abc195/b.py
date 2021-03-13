a,b,w=map(int,input().split())  # 120 150 2
w*=1000  # 2000
a_ans=w//a  # 16
a_mod=w%a  # 80
if a_mod/a_ans>b:
    if a_mod==0:
        pass
    else:
        print('UNSATISFIABLE')
        exit()
b_ans=w//b  # 13
b_mod=w%b  # 50
if b-(a-b_mod)/b_ans>=a:
    if b_mod==0:
        pass
    else:
        b_ans+=1
else:
    print('UNSATISFIABLE')
    exit()
print(b_ans,a_ans)

"""
120 150 2
14 16
"""
