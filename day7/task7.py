# Employee table using dictionary
emp_table = {
    "emp_name": "Arun",
    "id": 101,
    "phone_number": 9876543210,
    "address": "Chennai",
    "salary": 35000,
    "dept_no": 9,
    "dept_name": "IT",
    "mgm_id": 5,
    "mgm_name": "Suresh"
}

print("Original Employee Table:")
print(emp_table)

print("-" * 50)

# update() → update salary and address
emp_table.update({
    "salary": 40000,
    "address": "Bangalore"
})
print("After update():")
print(emp_table)

print("-" * 50)

# keys() → display all keys
print("Keys:")
print(emp_table.keys())

print("-" * 50)

# values() → display all values
print("Values:")
print(emp_table.values())

print("-" * 50)

# items() → display key-value pairs
print("Items:")
print(emp_table.items())

print("-" * 50)

# del → delete a key
del emp_table["phone_number"]
print("After deleting phone_number:")
print(emp_table)
