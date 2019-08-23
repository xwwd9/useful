


import re

#(\n | \xa0 | \[\d-\d\])

pattern = re.compile(r"(\n|\xa0|\[\d-\d\])")
text = "2234]5]4之材\n[3-4]\xa0\n。kk"
s = pattern.sub("", text)
print(s)
