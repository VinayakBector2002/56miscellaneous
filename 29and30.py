"""29. WAP to find the second largest number of a list
of numbers. Take the elements of list as input from
the user."""

list5= list(input('list5 : '))
list5.sort()
print('Second Largest digit :',list5[-2])

"""30. WAP to rotate the elements of a list so that
the element at the first index moves to the second
index, the element in the second index moves to the
third index, etc., and the element in the last
index moves to the first index."""

list_ = eval(input('Please enter a list : '))
k = list_[-1]
del list_[-1]
list_.insert(0,k)
print(list_)
