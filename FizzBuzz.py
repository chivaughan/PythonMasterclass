def FizzBuzz():
    number = int(input("Enter a Number: "))
    if number % 3 == 0 and number % 5 > 0:
        print("Fizz")
        return
    if number % 5 == 0 and number % 3 > 0:
        print("Buzz")
        return
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        return
    if number % 3 > 0 and number % 5 > 0:
        print(number)
        return


FizzBuzz()
