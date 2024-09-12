# Complete your individualized AI problems here

def fizzbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizzbuzz(1) == 1, "fizzbuzz 1 test"
assert fizzbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizzbuzz(4) == 4, "fizzbuzz 4 test"
assert fizzbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizzbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizzbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

import random

def guess_the_number(guess):
    num = random.randint(1, 101)
    if (guess < num):
        return 'Too low!'
    elif (guess > num):
        return 'Too high!'
    else:
        return 'That is correct! The number was' + str(guess)

print(guess_the_number(25))

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def calculator(a, b, operation):
    if operation == 'add':
        return a+b
    elif operation == 'subtract':
        return a-b
    elif operation == 'multiply':
        return a*b
    elif operation == 'divide':
        if b != 0:
            return a/b
        else:
            return 'Undefined'
    else:
        return 'Invalid operation!'

print(calculator(13, 66, 'multiply'))
print(calculator(6, 0, 'divide'))

def hours_to_minutes(hours):
    if hours > 0:
        return hours*60
    else:
        return 'Invalid amount.'
    
def add_numbers(a, b):
    return a+b