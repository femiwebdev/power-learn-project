my_list = []  # Create an empty list

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)  # Insert 15 at the second position

my_list.extend([50, 60, 70])  # Extend with another list

my_list.pop()  # Remove the last element

my_list.sort()  # Sort in ascending order

index_30 = my_list.index(30)  # Find the index of value

print("index of 30:", index_30)