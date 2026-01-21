# 1) Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("-" * 40)

# 2) Check positive or negative
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

print("-" * 40)

# 3) Check divisible by 5 or 7
num = int(input("Enter a number: "))
if num % 5 == 0 or num % 7 == 0:
    print("Divisible by 5 or 7")
else:
    print("Not divisible by 5 or 7")

print("-" * 40)

# 4) Check divisible by 2 and 3
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
else:
    print("Not divisible by both 2 and 3")

print("-" * 40)

# 5) Username and password check
username = input("Enter username: ")
password = input("Enter password: ")

if username == "sla" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
