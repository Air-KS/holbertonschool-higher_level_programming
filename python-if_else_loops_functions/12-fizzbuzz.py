#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
         # Vérifie les modulo
        if num % 3 == 5 and num % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(num), end="")
