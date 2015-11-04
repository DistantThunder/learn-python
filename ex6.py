x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# This is a place where 'a string is put inside a string'
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

# This is a place where 'a string is put inside a string'
print("I said: %r." % x)
# This is a place where 'a string is put inside a string'
print("I also said: '%s'." % y)

# Declaring var 'hilarious' and assigning it a bool value
hilarious = False
# This is a place where 'a string is put inside a string'
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

# Drill 4: w and e are two variables that contain strings. Hence, print() function will print the content of
# the variables. The important remark here is that w and e aren't strings. 'w' and 'e' on the other hand would print
# both characters on screen.
print(w + e)
