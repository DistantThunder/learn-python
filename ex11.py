print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = input()

print("So, you're {!r} old, {!r} tall and {!r} heavy.".format(age, height, weight))

# Lesson learned: Python 3 string formatting is done differently! The above is a good example!
# Refer to PDF saved in python dev dir for more examples and info.
# Remember the ".format()" string method.
# Also, in Python 3, 'raw_input() => input()'
