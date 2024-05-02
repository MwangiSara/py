# ELIF STATEMENTS

number=1001
if number<100: # condition 1
    print("is less than 100")
elif number==100: # condition 2
    print('is equal to 100')
else:
    print('is grater than 100')

# checking marks
grades=float(input("Enter your grade:"))
if grades<30:
    print("below average")
elif grades>=30 and grades<50:
    print("average")
elif grades>=50 and grades<70:
    print("above average")
else:
    print("excellent!")
    if grades==100:
        print("valedictorian")
    elif grades<0:
        print('invalid input')
    else:
        print("take test again")