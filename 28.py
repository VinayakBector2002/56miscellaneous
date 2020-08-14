"""28. WAP that inputs a list of numbers and shifts
all the zeros to right and all non-zero numbers to
left of the list."""

final = ''
list4 = list(input('list4 : '))
list4.sort()
list4.reverse()
for i in list4:
    final+=i
print(final)
