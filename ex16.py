from sys import argv

script, filename = argv

print("We're going to erase {!r}.".format(filename))
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going t write these to the file.")

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

print("And finally, we close it.")
target.close()

# Mistakes: typo.
