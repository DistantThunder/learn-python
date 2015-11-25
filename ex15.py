from sys import argv

script,  filename = argv

txt = open(filename, mode='r')

print("Here's your file {!r}:".format(filename))
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())



#Drills point: may be easier to pass filename as argv while invoking the script
#Rather than having to summon input. input() has its uses, but it's always better to have
#files that are to be processed by the program passed as CLI arguments