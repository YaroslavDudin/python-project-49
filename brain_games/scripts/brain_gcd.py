from brain_games.scripts.games.brain_gcd_game import random_num, main
import math 

rules = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    return math.gcd(a, b)


def generate_round():
    num1 = random_num(1, 100)
    num2 = random_num(1, 100)
    question = f"{num1} {num2}"  
    correct_answer = str(gcd(num1, num2))  
    return [question, correct_answer]


def start_brain_gcd():
    main(rules, generate_round)
