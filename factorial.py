__author__ = 'shubham'

# python programe to find the factorial of a no. provided by the user
def factorial(n) :
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1) # recursive call
def fact(n):
    for i in range (1 , n+1):
        print ("%2d! = %d" %(i, factorial(i)))
        try:
            var = int (input (" enter a number-"))
            fact (var)
        except Exception as e:
            print("error!!",e)
        else:
            print("you sucessfully entered integer")
if __name__== "__main__":
    fact(n)
    while True:
        again=input("do you want to process again:y/n-\n")
        if again=='y':
            even_odd()
        else:
            print("thank you for been here.....your are exiting from here.........bye bye!!!!")
            exit()


