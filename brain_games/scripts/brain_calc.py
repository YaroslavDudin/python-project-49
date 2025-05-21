
from brain_games.scripts.games.brain_calc_game import main
import secrets

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
    number1 = secrets.randbelow(25) + 1  
    number2 = secrets.randbelow(11) + 1  
    operators = ['+', '-', '*']
    operator = secrets.choice(operators)

    question = f'{number1} {operator} {number2}'
    correct_answer = str(calculate(number1, number2, operator))
    return [question, correct_answer]


def start_brain_calc():
    main(rules, generate_round)

