# Create an empty list
my_list = []

# Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Insert 15 at the second position of the list
my_list.insert(1, 15)
print(my_list)

# Extend my_list with another list
my_list.extend([50, 60, 70])
print(my_list)

# Remove the last element
my_list.pop()
print(my_list)

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30
print(my_list.index(30))

