number = int(input("Enter a number :"))
for x in range(number):
    print(" " * (number - x), "*" * (x * 2 + 1))