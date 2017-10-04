def hello( **args ):
    
    print()
    print()
    print("here is your dictionary",args)
    print()
    print()

    #print(args[:])
    #print("With for loop ")
    
    for var in args :
        print()
        print("key = ",var)
        print("value = ", args[var])
        print()

print("hello()")
hello()


print("\n\n hello(name = 'sachin', age = 21, addr = 'jaipur')")
hello(name = "sachin", age = 21, addr = 'jaipur')
print()

