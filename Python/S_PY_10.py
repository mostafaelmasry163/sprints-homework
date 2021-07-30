#   Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data

# - (Note) check if it is a valid email or not
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False


flag = 0

while flag < 1 :
    username = input("enter your name : ")
    if username != "" and not containsNumber(username) :
        flag = 1    
    else:
        print("enter a valid name")


flag = 0

while flag < 1 :
    useremail= input("enter valid email : ")
    if re.match(regex, useremail) :
        flag = 1
    else :
        print ("invalid email please try again")

print("your user name is ",username)
print("your email is ", useremail)
