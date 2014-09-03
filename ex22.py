# How about a make a math function that also uses a formatter, command line args, raw input and writes to a file

from sys import argv

script, operation = argv

first_number = float(raw_input('What is the first number you want to %s? ' % operation))
second_number = float(raw_input('What is the second number you want to %s? ' % operation))

to_file = raw_input('What file do you want to write the answer to? ')

def add(first_number, second_number):
  return first_number + second_number

def subtract(first_number, second_number):
  return first_number - second_number

def multiply(first_number, second_number):
  return first_number * second_number

def divide(first_number, second_number):
  return first_number / second_number

if operation == 'add':
  answer = add(first_number, second_number)

if operation == 'subtract':
  answer = subtract(first_number, second_number)

if operation == 'multiply':
  answer = multiply(first_number, second_number)

if operation == 'divide':
  answer = divide(first_number, second_number)

out_file = open(to_file, 'w')
out_file.write(str(answer))

print('Okay done')

out_file.close()