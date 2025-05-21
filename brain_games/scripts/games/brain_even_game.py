#!/usr/bin/env python3

import prompt
import random
import secrets

def is_even(number):
    return number % 2 == 0


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0
    while correct_answers_count < 3:
        number = secrets.randbelow(100) + 1
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if (is_even(number) == (answer == 'yes')):

            print('Correct!')
            correct_answers_count += 1
        else:
            correct_answer = 'yes' if is_even(number) else 'no'
            print(f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()


def random_num(min_val=1, max_val=100):
    
    return secrets.randbelow(min_val, max_val) 
