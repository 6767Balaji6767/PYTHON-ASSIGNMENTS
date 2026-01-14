# Initial list
name = ["abi", "akash", "alex"]
print("Original List:", name)

print("-" * 40)

# Get input from user and add to list
user_name = input("Enter a name to add: ")
name.append(user_name)
print("After user input:", name)

print("-" * 40)

# Accessing first element of the list
print("First element:", name[0])

print("-" * 40)

# a. Slice akash from the list
akash_name = name[1:2]
print("Sliced 'akash':", akash_name)

print("-" * 40)

# b. Add priya in the list
name.append("priya")
print("After adding priya:", name)

print("-" * 40)

# c. Add ajay and ajith in the list
name.extend(["ajay", "ajith"])
print("After adding ajay and ajith:", name)

print("-" * 40)

# e. Add jack between abi and akash
name.insert(1, "jack")
print("After adding jack between abi and akash:", name)
