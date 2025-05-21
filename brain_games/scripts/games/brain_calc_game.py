#!/usr/bin/env python3

import prompt
import random


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        return None  


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    correct_answers_count = 0
    operators = ['+', '-', '*']  

    while correct_answers_count < 3:
        num1 = random.randint(1, 20)  
        num2 = random.randint(1, 20)  
        operator = random.choice(operators)
        expression = f'{num1} {operator} {num2}'
        correct_answer = calculate(num1, num2, operator)

        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')

        try:
            answer = int(answer) 
        except ValueError:
            print(f"'{answer}' is not a valid number.  Please enter a number.")
            print(f"Let's try again, {name}!")
            return


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
    return random.randint(min_val, max_val)
