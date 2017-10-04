def hello( *args ):
    print()
    print()

    #print(args[:])
    #print("With for loop ")
    
    for var in args :
        print("Here is your args = ", var)


print("hello()")
hello()


print("\n\n hello(1,2,3,4,5,6)")
hello(1,2,3,4,5,6)


print("\n\nhello('python','helllo',1,2,3,4,5)")
hello("python", "helllo", 1, 2, 3,4,5)


print("\n\n hello([1,2,3],'hello','a','b')")
hello([1,2,3], "hello", 'a', 'b')
