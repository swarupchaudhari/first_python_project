def sum(*args):
    # args will be a tuple of all values passed
    total = 0

    for item in args:
        total += item

    return total


print(sum(342, 2, 7, 9))



  #kwargs
def marks(**kwargs):
    # kwargs is a dictionary of key-value pairs
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(shubham=34, vikrant=54, jack=34, marie=90, priya=45)



#args_kwargs.py
def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, jack=54, joyboy=24, marin=29)