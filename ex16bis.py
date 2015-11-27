from sys import argv

script, filename = argv

print("We're going to erase {!r}.".format(filename))
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("This is the new content of the file:\n")
print("Filename: {!r}".format(filename))
target.close()
print(open(filename, 'r').read())

print("\nAnd now we close {!r}.".format(filename))
