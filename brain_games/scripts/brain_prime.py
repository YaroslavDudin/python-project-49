from brain_games.scripts.games.brain_prime_game import random_num, main

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Checks if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    number = random_num(2, 100)  # Start from 2, as 1 is not prime
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return [question, correct_answer]


def start_brain_prime():
    main(rules, generate_round)

