def FizzBuzz():
    number = int(input("Enter a Number: "))
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


print(FizzBuzz())
