# In this Lesson we will Do Dta Types List, Tuples and Dictionary
# Define a List
# NB: ALways remind students that we count List items from Zero, Lists uses []
cars = ['Honda', 'Nissan', 'Surf', 'Mazda', 'Volkswagon']

# Print
print(cars)

# Accessing List items by index
print(cars[2])

# Slicing
# Print from index 2 to 5, There is a minus one
print(cars[2:6])

# Print from index 3 and above
print(cars[3:])

# Print upto index 4 and below, There is a minus one
print(cars[:5])

# List are mutable, Can be updated
# Lets Understand List Mutability
# Lets Update our List by Appending BMW into our List
cars.append("BMW")

# Now Print Your List
print(cars)  # Notice from output BMW is at Last

# Insert Toyota at a Given Position, Below we Insert Cars at Position 2
cars.insert(2, "Toyota")

# Now Print Your List, Notice Toyota at Position 2
print(cars)

# Next, What are Tuples? How do they Differ from Lists?