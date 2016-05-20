numbers = []

# while i < 6:
#     print("At the top i is {}".format(i))
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print("At the bottom i is {}\n{}".format(i, '-'))


def count_numbers(count):
    count += 1
    for i in range(0, count):
        numbers.append(i)
    return 0

count_numbers(int(input("Enter the number you want to count to: ")))
print("The numbers: ")

for num in numbers:
    print(num)
