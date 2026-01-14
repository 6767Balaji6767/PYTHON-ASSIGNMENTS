# Convert list into tuple
num_list = [1, 2, 3, 4, 5]
num_tuple = tuple(num_list)
print("Tuple:", num_tuple)

print("-" * 40)

# Set operations
g = {12, 18, 19, 20, 21, "hello"}
print("Original Set:", g)

# a. Add 100 in g
g.add(100)
print("After adding 100:", g)

# b. Add 22 and 25 in g
g.update([22, 25])
print("After adding 22 and 25:", g)
