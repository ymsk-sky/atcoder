s=input()
print('Yes' if s[::2]==s[::2].lower() and s[1::2]==s[1::2].upper() else 'No')
