# # Introduce For Loop. 
# # Modify the Parameters to how the Loop can print differently
# for index in range(5, 10, 1):
#     print(index)


# # Let the students to create some for loops  to output below;-
# # 1. From 50 to 100  Task1.py  
# # 2. From -10 to 10  Task2.py

Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
 
# Initialize matrix
matrix = []
print("Enter the entries row wise:")
 
# For user input
# A for loop for row entries
for row in range(Row):    
    a = []
    # A for loop for column entries
    for column in range(Column):   
        a.append(int(input()))
    matrix.append(a)
 
# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()