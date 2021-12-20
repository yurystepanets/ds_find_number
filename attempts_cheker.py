import numpy as np
from game_logic import random_predict

# Check avarage attempts count
def score_game(random_predict) -> int:
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000)) 

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    score_game(random_predict)