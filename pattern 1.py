def pattern():
    pattern()
def main():
    try:
        n = int(input("enter no. of rows-").strip())
    except Exception as e:
        print("error!!!!...try again",e)
    else:
        print("resultant pattern")
        for i in range(n):
           for j in range(i+1):
              print("*",end = '')
           print()
if __name__ =='__main__':
    main()
    while True:
        process_again=input("do you want to continue....y/n:").lower()
        if process_again == 'y':
            main()
        else:
            print("thankyou......\nyou are exiting to the program")
            exit()
