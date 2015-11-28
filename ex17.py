from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {!s} to {!s}".format(from_file, to_file))

# direct one liner
in_data = open(from_file).read()

print("The input file is {!d} bytes long".format(len(in_data)))

print("Does the output file exists? {!r}".format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# see context manager
# close resources when the exiting context: avoid leaving file object open for example
# when said fo where never given a representation through a variable.
with open(to_file, 'w') as out_file : out_file.write(in_data)

print("Alright, all done.")

in_data.close()

