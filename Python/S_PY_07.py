#  write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if it is divisible by both return "FizzBuzz"
number = int(input("enter a number: "))

def fizzbuzz(number) :
    for ele in range(number+1):
        if ele % 3 == 0 and ele % 5 == 0:
            print("Fizzbuzz")
            continue
        elif ele % 3 == 0:
            print("fizz")
            continue
        elif ele % 5 == 0:
            print("buzz")
            continue
        print(ele)

fizzbuzz(number)