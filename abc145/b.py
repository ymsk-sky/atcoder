n=int(input())
s=input()
print('Yes'if s[:len(s)//2]==s[len(s)//2:] else 'No')
