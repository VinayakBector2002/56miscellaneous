#23
#Mississippi
"""23. WAP to print the index of every í’ in
“Mississippi”"""

thr = "Mississippi"
for i in range (len(thr)):
    if (thr[i] == "i"):
        print(i)

#24
#slipt
"""24. WAP to display individual words of a sentence
taken as input using split( ) method."""

a = str(input('Enter a string : '))
l = a.split()
for i in l:
    print(i)



