n=int(input())
al='abcdefghijklmnopqrstuvwxyz'
ans=''
while not n<1:
    mod=n%26
    ans+=al[mod-1]  # mod=0: -1='z'
    n=n//26-1
print(ans[::-1])

"""
702=zz
702/26=27...0, 27/26=1...1
ans=z
n=27

703=aaa
703/26=27...1, 27/26=1...1
"""
