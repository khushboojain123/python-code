def pattern():
    n = int (input("enter no. of rows-"))
    for i in range(n):
        for j in range(i+1):
            print("*",end='')
        print()
def pattern1():
     n = int (input("enter no. of rows-"))
     for i in range(n):
        for j in range(n-i):
            print("*",end='')
        print()

if __name__ == '__main__':
    pattern()
    print()
    print()
    pattern1()

