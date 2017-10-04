
#python programe to check the input no is prime or not
#prime no are greater than 1

def prime():
    try:
        num = int(input("enter a no:").strip())
    except Exception as e:
        print("errorr!!!!!!..........",e)
    else:
        print("your output")
        if num > 1:
            count = 0
            for i in range (2,num):
                if(num % i)==0:
                    count+=1
            if count>0:
                    print(num,"is not prime no.")
            else:
                    print(num,"is a prime no")
        else:
            ("invalid input")
if __name__ == "__main__" :
    prime()
    while True:
        again=input("do you want to process again?: y/n=").lower()
        if again == 'y':
            prime()
        else:
            print("bye bye!!! you exiting the program")
            exit()

