__author__ = 'shubham'
def even(args):
    return even()    #function to return even no list
    """even(args)->this is a list which filters even no from a list.
    also return a list of even numbers.
        here args is common list of mixed no."""
def evenlist(args):
    return evenlist()
even=[]
args = input()
for item in args:
    if item % 2==0:
        even.append(item)
    print("welcome to even filtering,def of program-\n\n\n ",even.__doc__)
    print()
    print()
    print()
    n=int(input("enter no of items-"))
    l=[]
    print()
    while n>0:
        num=int(input())
        l.append(num)
        n-=1
        even_list = even(l)
        print()
        print("here is list of even no. = ",even_list)
        print()


