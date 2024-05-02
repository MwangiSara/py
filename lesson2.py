# boolean
is_actve=True
is_admin=False

print(type(is_actve))
print(type(is_admin))

# python lists
kindi=['Allan','Vincent','Solomon','sam','Esther', 1,55]
print(kindi)
print(type(kindi))
student=['name','john doe',['age',21],'phone number', 1]
print(student)
# slicing
print(student[1])
print(kindi[3:7])
print(kindi[:3])
# mutabilty
kindi.append('Ken')
print(kindi)
kindi.append('Ian')
print(kindi)
kindi.insert(5,'Jordan')
print(kindi)
kindi.pop(6)
print(kindi)
kindi.remove(55)
# number 8
list1=[10,20,[300,400,[5000,6000],500],30,40]
list1[2][2].append(7000)
print(list1)

