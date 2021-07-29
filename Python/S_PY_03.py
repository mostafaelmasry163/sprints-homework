# The program takes a string and a character and returns a list with all the locations that character was found in the given string.

# Implementation hint:

# String “Google” char ‘o’

# Output : [1,2]

string= input("enter a string ")
char= input("enter a char ")
output=[]
i=0

while i <= len(string)-1 :
    for letter in string :
        if char.lower() == letter.lower() :
            output.append(i)
            i +=1
        else :
            i +=1

print('output : ',output)