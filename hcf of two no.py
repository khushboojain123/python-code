
# Python program to find the H.C.F of two input number

# define a function
import time
def computeHCF(x, y):

# choose the smaller number89

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf
def main():
# take input from the user
    try:
       num1 = int(input("Enter first number: ").strip())
       num2 = int(input("Enter second number: ").strip())
       print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))
    except Exception as e:
        print("error!!!!!!!!...try again",e)
        main()
    else:
        print("good your input is valid and your result is as shown upper",)
        print("....")

if __name__ == '__main__':
    main()
    while True:
        again=input("do you want to process again:y/n-").lower()
        if again =='y':
            main()
        else:
            print("bye bye.........!!!!!you exiting from here")
            exit()


