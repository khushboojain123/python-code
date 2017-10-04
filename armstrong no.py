# python programe to find armstrong no.
#an armstrong no is the sum of the power of its digit is equals to the no. itself

def armstrong():
    return armstrong()

def main():
     num = int(input("Enter a number:-"))
     if num =='x':
        Break

     else:
      number = int (num)
      total = 0
      temp = number
      while temp > 0:
        digit = temp % 10
        total += digit **3
        temp //=10
     if number == total:

        print ("this is a armstrong no.=",num)

     else:
         print("this is not an armstrong no. =",num)


if __name__ =='__main__':
    main()
    while True:
        again = input("do you want to continue:y/n=\n").lower()
        if again == 'y':
            main()
        else:
            print("bye bye you are exiting from the program")
            exit()


