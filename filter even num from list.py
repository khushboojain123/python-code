def evenodd():
    return evenodd()


#start with empty list for even and odd numbers
def main():
    evens=[]
    odds=[]
    try:
        lower_range = int(input("enter a integer.-").strip())
        upper_range = int(input("enter a integer.-").strip())
    except Exception as e:
        print("error!!!",e)
    else:
        print("you sucessfully entered a integer")


        for num in range (lower_range ,upper_range+1):
            if num % 2 == 0 :
                evens.append(num)
            else:
                odds.append(num)
                print("evens",evens)
                print("odds",odds)

if __name__ == "__main__":
    main()
    while True:
        again=input("do you want to process again?: y/n=").lower()
        if again == 'y':
            main()
        else:
            print("bye bye!!! you exiting the program")
            exit()

