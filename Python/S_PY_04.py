# Given a list of numbers, create a function that returns a list where all similar adjacent elements have been reduced to a single element.



# So

# [1, 2, 2, 3, 2]

# Returns

# [1, 2, 3].


arr=[1,2,2,3,2,7,6,5,5,4,3,7]


def reducer(arr):
    newarr = []
    for ele in arr:
        if ele in newarr:
           continue 
        else:
           newarr.append(ele)
    print(newarr)

reducer(arr)

