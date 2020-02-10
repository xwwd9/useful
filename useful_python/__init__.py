import re

pattern = re.compile(r'.*?地\s*?址.*?')

a = "地址dd"

b = pattern.match(a)
print(b.end())
