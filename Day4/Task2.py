# Q1 Write a while loop that prints numbers from 1 to 5.
i = 1
while i <= 5:
    print(i)
    i += 1

# Q2 Write a for loop to iterate over a list of fruits and print each fruit.fruits = ["apple", "banana", "orange"]
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

#Q3 Write a loop (either while or for) that prints the first 3 multiples of 4.
for i in range(1, 4): # 1,2,3
    print(4 * i)
#Q4 Combine a for loop and an if statement to print only the vowels from a given word. word = "python"
    
word = "python"
v='aeiou'
for char in word:
    if char in v:
        print(char)

#Q5 Use either a while or for loop to reverse a given list. numbers = [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []
for num in reversed(numbers):
    reversed_numbers.append(num)
print(reversed_numbers)

