people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")

# Study Drills:
# 1. "if" evaluates the code under it only if the expression in front of it is True.
# 2. The code needs to be indented for the Python interpreter to understand that it is part of the "if" block.
# 3. If the code isn't indented by four spaces, it always gets evaluated by the interpreter,
# regardless of the 'if' statement.
# 4. The python interpreter throws an error on stdout about undefined "names" (variables).

