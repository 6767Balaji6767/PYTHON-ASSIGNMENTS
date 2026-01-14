# 1) Swap two numbers without using third variable
a = 10
b = 20
a, b = b, a
print("1) Swapped values:", a, b)

print("-" * 50)

# 2) Display three strings as “Name ** Is ** James”
print("2) Name ** Is ** James")

print("-" * 50)

# 3) Take an integer input from the user
num = int(input("3) Enter an integer: "))
print("You entered:", num)

print("-" * 50)

# 4) Print a variable inside a string
name = "James"
print(f"4) My name is {name}")

print("-" * 50)

# 5) Print a string multiple times
print("5) Hello " * 3)

print("-" * 50)

# 6) Print a string in reverse without using loops
s = "python"
print("6) Reversed string:", s[::-1])

print("-" * 50)

# 7) Take two numbers as input and print their sum
x = int(input("7) Enter first number: "))
y = int(input("   Enter second number: "))
print("Sum:", x + y)

print("-" * 50)

# 8) Take three numbers and print their average
a = int(input("8) Enter first number: "))
b = int(input("   Enter second number: "))
c = int(input("   Enter third number: "))
avg = (a + b + c) / 3
print("Average:", avg)

print("-" * 50)

# 9) Take a percentage as input and print with percentage sign
per = input("9) Enter percentage: ")
print("Percentage:", per + "%")

print("-" * 50)

# 10) Take a sentence and print it in uppercase, lowercase, and title case
sentence = input("10) Enter a sentence: ")
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
