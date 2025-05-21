
from brain_games.scripts.games.brain_calc_game import main
import random

rules = 'What is the result of the expression?'


def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    else:
        return None


def generate_round():
    number1 = random.randint(1, 25)  
    number2 = random.randint(1, 11)  
    operators = ['+', '-', '*']
    operator = random.choice(operators)

    question = f'{number1} {operator} {number2}'
    correct_answer = str(calculate(number1, number2, operator))
    return [question, correct_answer]


def start_brain_calc():
    main(rules, generate_round)

