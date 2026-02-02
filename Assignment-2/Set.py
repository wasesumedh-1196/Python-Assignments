
# Creating a Set
# Set egnores duplicate

collection = {1, 2, 2, 4, "Hello", "World", "World"}
print(collection)

# .add Method
# Inserting value

collection.add(3)
print(collection)

# .remove Method
# Deleting any value

collection.remove(4)
print(collection)

# .pop Method
# Shows any values

print(collection.pop())

# .clear Methode
# clears all set

collection.clear()
print(collection)

# .union Method
# combine all from both : egnore duplicate

set1 = {1, 2, 4, 3}
set2 = {3, 5, 2, 6}

print(set1.union(set2)) 

# .intersection
# combine all values from both : Only Same values

set1 = {1, 2, 4, 3}
set2 = {3, 5, 2, 6}

print(set1.intersection(set2))