#!/bin/python

#import pandas as pd

greet = 'Hello World'

name = 'John'

intruption = f'Hello {name}'

greet_fmt = 'Hello {}'

formatted = greet_fmt.format(name)

print(intruption, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace('John', 'Paul'))


NAMES = ['John', 'Paul', "George", "Ringo"]
AGES = [20,21,22,23]

JOHN = NAMES[0]
PAUL = NAMES[1]

#Slicing
JOHN_PAUL = NAMES[:2]
GEORGE_RINGO = NAMES[2:]

#STEPPING
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(REVERSE)
print(EVERY_OTHER)
print(max(AGES))

#two types of loops for and while (careful with while loops

name = "Jill"
interpolation = f"Hello, {name}"
print(interpolation)

greeting_format = "Hello, {}. How are you?"
formatted = greeting_format.format(name)