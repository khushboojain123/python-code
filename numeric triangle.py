def numtri():
    return numtri()
def main():

    try:
        n = int(input("enter no of rows-").strip())
    except Exception as e:
        print("error....!!!!!!!",e)
    else:
        print("good...valid input")
        for i in range(1,n+1):
            for j in range(i):
                print(i,end ='')
            print()

if __name__=='__main__':
    main()
    while True:
        again=input("do you want to process again:y/n:-").lower()
        if again == 'y':
            main()
        else:
            print("bbyeee....!!!!!!thanank you for being here will meet again")
            exit()

