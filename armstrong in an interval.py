# program to display all the armstrong number in which interval which is given by user
# take input from user
def arm():
    
    return()

def main():
    lower = int(input("enter lower range:"))
    upper= int(input("enter upper range:"))
    for num in range(lower, upper+1):
        sum=0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum +=digit **3
            temp//=10
            if num == sum:
                print(num)

if __name__ == "__main__":
    main()
    while True:

        again =input("do you want to continue y/n").lower()

        if again == 'y':
            main()
        else:
            print("thank you,you are exiting from the program")
            exit()

