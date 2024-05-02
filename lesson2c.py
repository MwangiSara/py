#dictonary
john_doe={
    'name':'john doe',
    'national ID':101,
    'age':25,
    'address':60050,
    'favourite color':["blue",'black']
}
print(john_doe)
print(type(john_doe))
print(john_doe['national ID'])
# appending
john_doe['car']='BMW'
print(john_doe)
# update
john_doe['age']=35
print(john_doe)
# deleting
del john_doe['address']
print(john_doe)