# while loop
num1=0
while num1<=10:
    print(num1)
    num1+=1 #num1=num1+1 ie 0=0+1 1=1+1 2=2+1

num3=10
while num3<=20:
    print(num3)
    num3+=2

index=1
total=0
while index<=10:
    total+=index #total=total+index
    index+=1
print(total)

index2=40
total1=0
while index2<=60:
    total1+=index2
    index2+=2
print(total1)

# matrix
row=int(input("enter the number of rows:"))
col=int(input('Enter the number of columns'))
# initialize matrix
matrix=[]
print('enter the entries row wise:')
for row1 in range(row):
    a=[] #a for loop for column entries
    for col1 in range(col):
        a.append(int(input()))
    matrix.append(a)
# for printing the matrix
for row1 in range(row):
    for col1 in range(col):
        print(matrix[row1][col1], end="")
    print()
