"""Игра угадай число от 1 до 100
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=50, guess_min:int=1, guess_max:int=100)->int:
    """Угадываем число случайным образом

    Args:
        number (int, optional): Загаданное число. Defaults to 50.
        guess_min (int, optional): Minimum value of the guessing interval. Defaults to 1.
        guess_max (int, optional): Maximum value of the guessing interval. Defaults to 100.


    Returns:
        int: Число попыток угадывания
    """

    count = 0
    
    while True:
        count += 1
        
        # Предполагаем, что загаданное число - середина интервала
        predict_number = round((guess_min + guess_max)/2)
        
        # если ширина интервала больше 1
        if guess_max - guess_min > 1:  
            if number == predict_number:
                break # число угадано, выходим из цикла
            elif number < predict_number:
                guess_max = predict_number
            elif number > predict_number:
                guess_min = predict_number
                
        # Если ширина интервала меньше или равно 1,
        # то либо его минимальное значение - загаданное число,
        # либо - максимальное значение.
        elif number == guess_min:
            break # число угадано
        elif number == guess_max:
            count += 1
            break # число угадано
        
    return count

def score_game(random_predict, guess_min:int=1, guess_max:int=100)->int:
    """Определяет среднее кол-во попыток, необходимых алгоритму для угадывания числа

    Args:
        random_predict ([type]): Guessing function.
        guess_min (int, optional): Minimum value of the guessing interval. Defaults to 1.
        guess_max (int, optional): Maximum value of the guessing interval. Defaults to 100.

    Returns:
        int: среднее кол-во попыток угадывания
    """
    
    count_ls=[] # список, хранящий кол-во попыток угадывания
 #   np.random.seed(1)    # фиксируем последовательность случайных чисел, задав значение seed
    random_array = np.random.randint(guess_min, guess_max+1, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number, guess_min, guess_max))
        
    score = int(np.mean(count_ls))  # определяем среднее кол-во попыток
    print(f"Ваш алгоритм угадывает число от {guess_min} до {guess_max} в среднем за {score} попыток")
    
    return score

if __name__ == '__main__':
    # RUN
    score_game(random_predict)