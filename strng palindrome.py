#programe to check if a string is palindrome or not
#take input from user

def strpalindrome():
    return()

def main():
    try:
        my_str = input("enter a string:")
    except Exception as e:
        print("errorr!!!!!!........",e)
    else:
        print("here is your result-") 
        my_str = my_str.casefold()         #make it suitable for caseless comparision
        rev_str = reversed(my_str)         #reverse the string
                                           #check if string is equal to its reverse
        if list(my_str) == list(rev_str):
            print("it is palindrome")
        else:
            print("it is not a palindrome")

if __name__ == '__main__':
    main()
    while True:
        again=input("do you want to process again:y/n-").lower()
        if again =='y':
            main()
        else:
            print("bye bye.........!!!!!you exiting from here")
            exit()

