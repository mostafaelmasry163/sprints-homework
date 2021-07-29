# The program takes a string and remove the vowels character from it then print its new version

# Implementation hint:

#                        So, “Mobile” becomes “Mbl”

vowels = ['a','e','o','u','i','A','E','O','U','I']
string= input("enter a string ")
newstring = ""
for letter in string :
        if letter in vowels :
            continue
        else :
            newstring += letter

print(newstring)