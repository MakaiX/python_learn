import re

pattern = re.compile(r'\d+')
split_p = re.compile(r'[\s,;]+')
p_sub = re.compile(r'(\w+) (\w+)')

m = pattern.match("one2two0three34four", 3, 10)
print(m)

search = pattern.search('one12two0three34four')
print(search)

findall = pattern.findall('one12two0three34four')
print(findall)

finditer = pattern.finditer('one12two0three34four')
print(finditer)
for i in finditer:
    print(i.group())

split = split_p.split('a,b ; c   d')
print(split)

s = 'hello 123, hello 456'

sub = p_sub.sub('Hello World', s)
print(sub)
print(p_sub.sub(r'\2,\1', s))

18519149790