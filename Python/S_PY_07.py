#  write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if it is divisible by both return "FizzBuzz"
number = int(input("enter a number: "))


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else :
        print(number)


fizzbuzz(number)
