def even_odd():
    try:
        num = int (input ("enter a number-"))
    except Exception as e:
        print("error!!!!!!!!!!.........try again",e)
        even_odd()
    else:
        print("your result is that")
        if num > 1:
            if (num % 2) == 0:
                print ("the number you entered is even number")
            else:
                print ("the number you entered is odd number")

if __name__== "__main__":
    even_odd()
    while True:
        again=input("do you want to process again:y/n-\n")
        if again=='y':
            even_odd()
        else:
            print("thank you for been here.....your are exiting from here.........bye bye!!!!")
            exit()


