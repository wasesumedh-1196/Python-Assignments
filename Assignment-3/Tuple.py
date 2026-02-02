
# Blank Tuple
tup = ()
print(tup)
print(type(tup))

# Create 1st Tuple
tup1 = (33.4, 48.9, 43.3, 82.7)
print(tup1)

# Print Any Element From Tuple 1
print(tup1[1])

# Create 2nd Tuple
tup2 = (63, 27, 28, 34)
print(tup2)

# Print Any Element From Tuple 2
print(tup2[2])

# Nesting Of Tuples
nested_tuple = (tup1,tup2)
print(nested_tuple)

# Concatinate Both Tuples
Concatinated_Tuple = tup1 + tup2
print(Concatinated_Tuple)

# indexing A Tuple
# Print Any Number Using Index

tup = (1, 3, 2, 1, 2, 3)
print(tup.index(3))

# Counting Methode
# How much time this number is present

tup = (1, 3, 2, 1, 2, 3)
print(tup.count(3))