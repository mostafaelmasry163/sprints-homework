#  Write a function that accepts two arguments (length, start) to generate an array of a specific length filled with integer numbers increased by one from start.

leng=int(input("enter length of the array: "))
start=int(input("enter the starting number: "))

def array_generator(leng,start) :
    arr=[start]
    i=1
    while i<leng :
        arr.append(start+i)
        i+=1
    return arr

print(array_generator(leng, start))