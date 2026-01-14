# String methods example
str1 = "python"

print("Upper:", str1.upper())
print("Lower:", str1.lower())
print("Capitalize:", str1.capitalize())
print("Count of 'o':", str1.count('o'))
print("Title:", str1.title())

print("-" * 30)

# Replace java with python
str2 = "java is easy to learn"
replaced_str = str2.replace("java", "python")
print("Replaced String:", replaced_str)

print("-" * 30)

# Split the string
split_str = str2.split()
print("Split String:", split_str)

# Join the string
joined_str = " ".join(split_str)
print("Joined String:", joined_str)

print("-" * 30)

# Using strip and split
str3 = "   java is easy    to learn   "
clean_str = str3.strip()
final_list = clean_str.split()

print("After strip():", clean_str)
print("After split():", final_list)
