#26 
"""Given two lists, WAP that prints
“Overlapped” if they have at least one member
in common, otherwise prints “Separated”. Use
for loop."""
list1 =list(input('Enter list 1  '))
list2 =list(input('Enter list 2  '))
print(list1)
print(list2)
overlap = False
for i in list1:
    for j in list2:
        if i == j:
            overlap = True
if overlap :
    print('Overlap')
else :
    print('Seperated')
