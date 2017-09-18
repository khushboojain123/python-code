#this is map function
fact = lambda n: 1 if n ==1 else n*fact(n-1)
l = [1,2,3,4,5,6]
r = list(map(fact,l))
print(r)

#our map function
def map(func,seq):
    list =[]
    for var in seq:
        k = func(var)
        list.append(k)
    return list
reslt = map(fact,l)
print(reslt)
