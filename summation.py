def add (*args):
    """add (*args)->This is a function which performs the summation of n numbers.
    here *args is multiple argument as tuple."""
    s=0
    for var in args:
        for i in var:
            s+=i
        return s
print("welcome to sum of number program,def of program- \n ", add.__doc__)

n=int(input("enter no of items-"))
l=[]

while n>0:
    num=int(input())
    l.append(num)
    n-=1
result=add(l)
print("sum of no.=",result)


