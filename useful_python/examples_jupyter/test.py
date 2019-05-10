def func(a):
    a['1']['a'][0] = 20
    return a


b = {'1': {'a': [[10]]}}
c = func(b)
print(b == c)
