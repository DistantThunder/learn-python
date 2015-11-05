from sys import argv

script, user_name = argv
prompt = '> '

print("Hi {!s}, I'm the {!s} script.".format(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me {!s}".format(user_name))
likes = input(prompt)

print("Where do you live {!s}?".format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {!r} about liking me.
You live in {!r}. Not sure where that is.
And you have a {!r} computer. Nice.
""".format(likes, lives, computer))