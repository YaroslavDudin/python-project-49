#!/usr/bin/env python3

import prompt
import math  
import secrets


def gcd(a, b):
    return math.gcd(a, b)


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    correct_answers_count = 0

    while correct_answers_count < 3:
        num1 = secrets.randbelow(100) + 1
        num2 = secrets.randbelow(100) + 1
        correct_answer = gcd(num1, num2)

        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')

        if not answer.isdigit():
            print(f"'{answer}' is not a valid number. Please enter a number.")
            print(f"Let's try again, {name}!")
            return

        answer = int(answer)

        if answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()


def random_num(min_val=1, max_val=100):
    return secrets.randbelow(max_val - min_val) + min_val

