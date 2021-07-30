#   Write a function that takes a string and prints the longest alphabetical ordered substring occured.



# For example, if the string is 'abdulrahman' then the output is:

# Longest substring in alphabetical order is: abdu

longString = input("enter a long string of characters : ")
long = longString[0]
current = longString[0]


for char in longString[1:]:
    if char >= current[-1]:
        current += char
        if len(current) > len(long):
            long = current
    else:
        current = char


print ("Longest substring in alphabetical order is:", long)
