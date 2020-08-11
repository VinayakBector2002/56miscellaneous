#Q22
"""22. WAP to perform the following tasks:
i. Take a word as input from the user
ii. Use a for loop to display each letter in
the word
iii. Print each letter in reverse order
iv. Make a new string that is the reverse of
original string and print the variable
v. Count the number of characters in the word
without using any inbuilt functions. """
#a = str(input('Enter a string : '))

print('Each letter of : ')
for i in a:
    print(i)
print('Reverse order;')
aRev = a[::-1]
for j in aRev:
    print(j)
print('The New string in rev order :',aRev)
length=0
for i in a:
    if i.isspace():
        length+=1
print('No. of words :', length+1)

