#program to make a simple calculator

#define function
def add(a,b):
    """this function add two number"""
    return a+b
def sub(a,b):
    """this function substract two number"""
    return a-b
def mul(a,b):
    """this function multiplies two numbers"""
    return a*b
def div(a,b):
    """this function divide two number"""
    return a/b
def mod (a,b):
    return a%b

def main():
    try:
        ch = int(input("1.add\n2.sub\n3.mul\n4.div\n5.mod\ninput- ").strip())
    except ValueError as e:
        print("error!!!!!.......",e)
        main()
    else:
        print()
    try:
        x = int(input("enter a no. - ").strip())
        y = int(input("enter a no. - ").strip())
    except Exception as e:
        print("there was an error.....",e)
    else:
        print()
    if ch == 1:
        print("result is - " ,add(x,y))
    elif ch == 2:
        print("result is - " , sub(x,y))
    elif ch == 3:
        print("result is - ", mul(x,y))
    elif ch == 4:
        print("result is - ", div(x,y))
    elif ch == 5:
        print("result is - ",mod(x,y))
    else:
        print("invalid choice - try again")

    ch1 = input("do you want to continue -y/n-")
    if ch1.lower() == 'y':
        main()
    else:
        exit(0)

if __name__ =='__main__':
    main()
