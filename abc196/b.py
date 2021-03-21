x=input()
print(x[:x.find('.')] if '.' in x else x)
