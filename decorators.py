def info(**kwargs):
    for name in kwargs:
        print("hello!!!" ,name)

def info(**kwargs):
    for name in kwargs:
           print("hello!!! key= ", " value = ", kwargs[name])

info(name = 'khushboo' ,age = 21 , addr = 'jaipur')


def decorator(old_value):
    def inner(**kwargs):
        for var in kwargs:
            print(name, "=", kwargs[var])
    return inner


def decorate(old_fun):
    def inner(**kwargs):
        print(var, "=" ,kwargs[var])
    return inner

new_info = decorate(info)
new_info(name = 'khushboo' , age = 21, addr = 'jaipur')


