str = input()
alpha = list(str)
result = ""

for i in alpha:
    if i.isupper():
        result += i.lower()
    else:
        result += i.upper()

print(result)
