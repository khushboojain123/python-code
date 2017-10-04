
# prints a line segment
def draw_line():
    return draw_line()

def main():
    try:
        raw_input=(input()).strip()
    except Exception as e:
        print("error!!!",e)
    else:
        print("you suceffuly entered input")
        count = 0
        while ( count < 100 ):
            count = count+1
            print(raw_input,end = '')

if __name__ == "__main__":
    main()
    while True:
        again =input("do you want to draw line again y/n:\n").lower()
        if again =='y':
            main()
        else:
            print("thank you ,you are exiting from the program")
            exit()

