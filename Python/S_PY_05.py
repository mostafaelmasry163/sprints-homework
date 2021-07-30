#   Consider dividing a string into two halves.

# Case 1:

# The length is even, the front and back halves are the same length.

# Case 2:

# The length is odd, we'll say that the extra char goes in the front half.



# e.g. 'abcde', the front half is 'abc', the back half 'de'.

# Given 2 strings, a and b, return a string of the form :

# (a-front + b-front) + (a-back + b-back)

a='abcd'
b='xyz'



def strslice(str):
    if len(str) % 2 == 0 :
        res_first, res_second = str[:len(str)//2],str[len(str)//2:]
    else :
        res_first, res_second = str[:(len(str)//2)+1],str[(len(str)//2)+1:]
    
    return res_first,res_second


asliced = strslice(a)
bsliced = strslice(b)

print(asliced[0]+bsliced[0], asliced[1]+bsliced[1])
