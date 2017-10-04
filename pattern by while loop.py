def pattern():
    i = 2
    n = int (input("enter no. of rows-"))
    while i <= n :
        j=n
        while j > 0:
            if i > j:
                print("*",end='')
            else :
                print(' ',end='')
            j-=1
        print()
        i +=1
if __name__ == '__main__':
    pattern()


