#  Write a function which has an input of a string from user then it will return the same string reversed
########################
######### solution 1

# strin = input("enter a word : ")

# def reve_str (str) :
#     revestrin =""
#     leng = len(str)
#     while leng > 0 :
#         revestrin += str[leng-1]
#         leng -=1


#     return revestrin

# print("the string reversed is "+reve_str(strin))

#################################
### Another solution

strin = input("enter a word : ")
def reverse_string(word) :
    if word == "" : return "" 
    last = word[-1]
    els = word[0:-1]
    return last + reverse_string(els)

print("the string reversed is " + reverse_string(strin))
