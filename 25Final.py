#Q25

#SubstringCount
""" 25. WAP to take a string and a substring from the
user. It should then display the number of
occurrences of the given substring in the line. """

string = input(str("Ënter a sentence "))
substr = input(str("Ënter a sub strng "))
l=[]
count = 0
l = string.split()
for i in l:
    if i == substr :
        count+=1
print('Count of substring', substr, 'in the string', string, 'is', count)

print("EOP")
