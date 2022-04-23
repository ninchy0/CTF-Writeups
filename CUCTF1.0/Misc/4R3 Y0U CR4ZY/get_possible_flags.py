
sanitized = []
unique = []

with open('flags.txt', 'r') as f:
    x = f.readlines()
    for i in x:
        sanitized.append(i.replace('\n', ''))

for i in sanitized:
    if i not in unique:
        unique.append(i)

print(unique)
