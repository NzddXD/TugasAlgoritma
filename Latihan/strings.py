# String
text = 'those who knows toma toma'

# Indexing
print(text[0])

# Slicing
print(text[0:8])

# Methods
upper = str.upper(text)
lower = str.lower(text)
split = str.split(text)
replace = text.replace('knows', 'goons')

joinContent = ['hello', 'neighbor']
join = "=".join(joinContent)

print(join)