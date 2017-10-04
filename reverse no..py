#python code to reverse the number

def rev():
   return rev()
def main():
     try:
        n = int (input ("enter a no - ").strip())
     except Exception as e:
        print("error...........",e)
        main()
     else:
         print()
     s = str(n)
     temp = s[::-1]
     N = int(temp)
     print("Reverse of no.",n,"is=",N)
     if n == N:
         print (n,"is palindrome")
     else:
         print(n,"is not palindrome")

if __name__ == '__main__':
    main()
    again=input("do you want to process again:y/n-:").lower()
    if again == 'y':
        main()
    else:
        print("bye bye.........!!!!!!")