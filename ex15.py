from sys import argv

script,  filename = argv

txt = open(filename, mode='r')

print("Here's your file {%r}:".format(filename))
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
