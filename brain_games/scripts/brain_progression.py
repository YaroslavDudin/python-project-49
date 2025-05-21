from brain_games.scripts.games.brain_progression_game import random_num, main


rules = 'What number is missing in the progression?'


def generate_progression(start, step, length=10):
    return [start + i * step for i in range(length)]


def generate_round():
    start = random_num(1, 20)
    step = random_num(2, 5) 
    progression = generate_progression(start, step)
    hidden_index = random_num(0, len(progression) - 1)  

    hidden_number = progression[hidden_index]
    progression[hidden_index] = '..'  

    question = ' '.join(map(str, progression))  
    correct_answer = str(hidden_number)  

    return [question, correct_answer]


def start_brain_progression():
    main(rules, generate_round)
