# Guess the number

import random

answer = random.randint(0,101)
name = input('What is your name?')
print('Hello, ',name)
print('I am thinking of a number. Can you guess what is it?')
for i in range(1, 7):
    num = int(input())
    if num < answer:
        print('Too low')
    elif num > answer:
        print('Too high')
    else:
        break

if num == answer:
    print('win. took ', i, ' guesses')
else:
    print('nope, it is ', answer)
