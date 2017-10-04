# this is filter function

l = [1,2,34,5,7,55,67,89,70,56,71,24,60]
result = list(map(lambda x:'even' if x %2 == 0 else 'odd' ,l))
print(result)


feven = filter(lambda x: False if x%2 else True, l)
feven = list(feven)
print(feven)


fodd = filter(lambda x: True if x%2 else False, l)
fodd = list(fodd)
print(fodd)
