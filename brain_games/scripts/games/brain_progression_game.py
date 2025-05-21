#!/usr/bin/env python3

import prompt
import random


def generate_progression(start, step, length=10):
    return [start + i * step for i in range(length)]


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    correct_answers_count = 0

    while correct_answers_count < 3:
        start = random.randint(1, 20)
        step = random.randint(2, 5)  
        progression = generate_progression(start, step)
        hidden_index = random.randint(0, len(progression) - 1)  

        hidden_number = progression[hidden_index]
        progression[hidden_index] = '..'  

        question = ' '.join(map(str, progression)) 

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        try:
            answer = int(answer)
        except ValueError:
            print(f"'{answer}' is not a valid number. Please enter a number.")
            print(f"Let's try again, {name}!")
            return

        if answer == hidden_number:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{hidden_number}'.")
    
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()


def random_num(min_val=1, max_val=100):
    return random.randint(min_val, max_val)
