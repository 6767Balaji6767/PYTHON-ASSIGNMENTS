# Sorting and reversing a list
num = [10, 7, 2, 1, 18]
print("Original List:", num)

num.sort()
print("Sorted List:", num)

num.reverse()
print("Reversed List:", num)

print("-" * 40)

# Combine two lists
list1 = [1, 2]
list2 = [2, 3]
combined_list = list1 + list2
print("Combined List:", combined_list)

print("-" * 40)

# Remove java from the list
course = ["python", "java", "django"]
print("Original Course List:", course)

course.remove("java")
print("After removing java:", course)

print("-" * 40)

# Convert list into set
course_set = set(course)
print("Converted Set:", course_set)
