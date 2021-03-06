#!/usr/bin/env python3

print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Custom try at alignment using format spec
print("{:^30}".format('-------------'))
print(poem)
print("{:^30}".format('-------------'))


five = 10 - 2 + 3 - 6
print("This should be five: {:d}".format(five))


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates, = secret_formula(start_point)

print("With a starting point of {:d}".format(start_point))
print("We'd have {:d} beans, {:.0f} jars, and {:.0f} crates.".format(beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have {0[0]:.0f} beans, {0[1]:.0f} jars, and {0[2]:.0f} crates.".format(secret_formula(start_point)))

