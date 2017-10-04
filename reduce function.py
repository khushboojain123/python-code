from functools import reduce
l = [1,2,3,4,5,6,7,8,9]
k = reduce(lambda x,y:x+y,l)
print(k)

k = reduce (lambda x,y :x+y , [var for var in range(6)])
print(k)