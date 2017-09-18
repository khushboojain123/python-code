__author__ = 'shubham'

# python programe to find the factorial of a no. provided by the user


def factorial (n) :
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1) # recursive call
def fact(n):
    for i in range (1 , n+1):
        print ("%2d! = %d" % (i, factorial(i)))

var = int (input (" enter a number-"))
fact (var)

