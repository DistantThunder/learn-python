# a function similar to the previous examples with argv

def print_two(*args):
    arg1, arg2 = args
    print("arg1: {!r}, arg2: {!r}".format(arg1, arg2))


# compare with previous function, no need for *args

def print_two_again(arg1, arg2):
    print("arg1: {!r}, arg2: {!r}".format(arg1, arg2))


# This function just takes one argument

def print_one(arg1):
    print("arg1: {!r}".format(arg1))


# And this one takes none

def print_none():
    print("I got nothin'.")


print_two("Corvus", "MK ULTRA")
print_two_again("Nova 6", "POTUS")
print("First!")
print_none()
