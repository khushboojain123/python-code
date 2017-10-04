import os,sys,shutil

def choice():


    ch = int(input("enter your choice \n1.open file \n 2.write file \n 3.create file \n 4.delete file \n 5.copy file \n 6.move file\n 7.rename_file\n 8.cwd \n 9.exit \n "))
    if ch == 1:
        open_file()
    elif ch == 2:
        write_file()
    elif ch == 3:
        create_file()
    elif ch == 4:
        delete_file()
    elif ch == 5:
        copy_file()
    elif ch == 6:
        move_file()
    elif ch == 7:
        rename_file()
    elif ch == 8:
        cwd()
    elif ch == 9:
        print("bye bye..........exiting text editor")
        exit(0)
    else:
        print("wrong input ,try again")
        choice()


def open_file():
    file_path = input("enter full path to your file- ")
    if os.path.exists(file_path):
        with open(file_path) as fp:
            print(fp.read())
            choice()
    else:
        print("file does not exists \n do you want to create a new file y/n-")
        input().lower() == 'y'
        create_file(path = None)
        choice()


def write_file():
    try:

        file_path = input("enter full path to your file-")
        if os.path.exists(file_path):
            with open(file_path , 'a+') as fp:
                print("start writing into file- press:wq for save and exit")
                while True:
                    temp = input()
                    if temp ==':wq':
                        print("save and exiting your file")
                        choice()

                    else:
                        fp.write(temp)
                        fp.write('\n')
        else:
             print("file does not exists")
             choice()
    except Exception as e:
        print("there was a problem: %s",(e))



def create_file(path = None):
    try:
        if path:
            file_path = path
        else:

            file_path = input("enter full path to your file-")
            with open(file_path,'w+') as fp:
                print("start writing into file - press :wq save and exit")

                while True:
                    temp = input()
                    if temp == ':wq':
                        print("saving and exiting the file")
                        choice()
                    else:
                        fp.write(temp)
                        fp.write('\n')
    except Exception as e: 
         print("there was a problem: %s",(e))
                

def delete_file():
    try:
        file_path = input("enter your file path which you want to delete-")
        if os.path.exists(file_path):
            os.unlink(file_path)
            print("file sucessfully deleted")
            choice()
        else:
            print("no such file exist")
            choice()
    except Exception as e:
        print("there was a problem: %s",(e))


def copy_file():
    source_path = input("enter full source file_path-")
    dest_path = input("enter full destination file path-")
    if os.path.exists(source_path):
        shutil.copy(source_path , dest_path)
        print("file sucessfully copied")
    else:
        print("file does not exists")
        choice()

def move_file():
    source_path = input("enter path which file do you want to move-")
    dest_path=input("enter new path where do you want to move your file")
    if os.path.exists(source_path):
        shutil.move(source_path , dest_path)
        print("file sucessfully moved")
    else:
        print("file does not exists")
        choice()

def rename_file():
    old_path = input("enter old path of file which you want to rename")
    new_path = input("enter new path")
    if os.path.exists(old_path):
        os.rename(old_path ,new_path)
        print("file sucessfully renamed")
        choice()
    else:
        print("file does not exists")
        choice()

def cwd():
    try:
        print(os.getcwd())
        change = input("do you want change dir Y/N:")
        if change.startswith("y"):
            path = input("new cwd:")
            os.chdir(path)
    except Exception as e:
        print("there was a problem: %s"%(e))


if __name__ == '__main__':
    print("welcome to command line text editor")
    choice()



