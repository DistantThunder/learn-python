my_name = 'Darkeox'
my_age = 35  # is it?
my_height = 185  # centimeters
my_weight = 75  # kilos
my_eyes = 'Dark Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s." % my_name)
print("He's %d centimeters tall." % my_height)
print("He's %d kilos heavy." % my_weight)
print("Actually, that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))

# this line is tricky
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

# Drill 4. The only one I found interesting
# Convert Centimeters and Kilos into inches and pounds

# value of 1 pound for in kilo
pound = 0.45359237  # kilo

# value of 1 inches in centimeters
inch = 2.54  # centimeters

my_height_inches = my_height / inch
my_weight_pounds = my_weight / pound

print("Using the imperial customary system of measurement, "
      "we can also say that he is %d inches tall and %d pounds heavy." % (my_height_inches, my_weight_pounds))
