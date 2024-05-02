# FOR LOOP
for index in range(7):
    print(index)

for index2 in range(20,51):
    print(index2)

for index3 in range(20,51,2):
    print(index3)

for index4 in range(20,50):
    if index4==30:
        break
    print(index4)

name=['jane','john','james','done']
for x in name:
    print(x) 

countries=('Kenya','malawi','fiji','denmark','congo')
for y in countries:
    print(y)

fruits=['banana','apple','blueberry','mango']
for f in fruits:
    if f=="blueberry":
        continue
    print(f)

for x in range(6):
    #leave it empty
    pass