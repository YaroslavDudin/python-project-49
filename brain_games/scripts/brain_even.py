from brain_games.scripts.games.brain_even_game import random_num, main
    
    

rules = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
def generate_round():
    question = random_num(1, 100)
    correct_answer = "yes" if is_even(question) else "no"
    return [question,correct_answer]
def start_brain_even():
    main(rules , generate_round)

