import numpy as np

def game_core_v4(number,min_number=1,max_number=101):
    '''Guess the number game enveloped in a function.
       Algo used for guessing: binary search -- narrow down the interval from
       both ends with min_number (inclusive), max_number (exlusive) variables'''
    count = 0
    while True:
        count += 1
        predict = (min_number + max_number)//2
        #print(count,":",min_number,number,max_number,f"({predict})") # TRACE
        if number == predict:
            break  # exit when guessed right
        elif number > predict:
            min_number = predict + 1
        else:  # number < predict: 
            max_number = predict - 1
    return(count)


def score_game(game_core):
    '''Run game 5000 times to get the guess attempt statistics'''
    count_ls = []
    np.random.seed(1)  # fixed random seed to allow reproducible execution
    from_number = 1
    to_number = 101
    random_array = np.random.randint(from_number,to_number, size=(5000))
    for number in random_array:
        count_ls.append(game_core(number,from_number,to_number))
        #print("-") # TRACE
    score = int(np.mean(count_ls))
    return(score)


def run_demo():
    score_v4 = score_game(game_core_v4)
    print(f"The algorithm guesses the right number with {score_v4} attempts.")

# Execute main
run_demo()
