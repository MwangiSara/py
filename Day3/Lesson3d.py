#  Lets Look at a students perfomance scenario .
#  We will include Comparison and Logical Operators
marks = float(input('Enter Students Marks: '))
# marks = 78

if marks < 30:
    print("Below Average")

elif marks >=30 and marks < 40:
    print("Average")

elif marks >=40 and marks < 70:
    print("Above Average")

else:
    print("Excellent!")
    # Nested Ifs, If statements inside another,
    # Below nested if means Only whoever gets 100 gets an Award.
    if marks == 100:
        print("You will get an award")