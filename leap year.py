
#python programe to check year is leap year or not
def leap():
    return leap()
def main():
    try:
        year = int(input("enter a year-").strip())
    except Exception as e:
        print("error!!!",e)
    else:
        print("nice..you entered a valid input")
        if (year % 4)== 0:
            if (year % 100) ==0:
                if (year % 400)==0:
                     print("{0} is leap year" .format (year))

                else:
                     print ("{0} is not leap year". format(year))

            else:
                 print ("{0} is leap year".format(year))

        else:
             print ("{0} is not leap year" .format(year))
if __name__ == '__main__':
    main()
    while True:
       again= input("do you want to process again:y/n:").lower()
       if again=='y':
           main()
       else:
           print("bye bye..........!!!\nyou exit from the program")
           exit()