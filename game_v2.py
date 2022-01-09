import numpy as np

def random_predict(number:int=1)->int:
    """Угадываем число случайным образом

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток угадывания
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,501)  # Компьютер генерит предполагаемое число
        if number == predict_number:
            break # число угадано, выходим из цикла
        
    return count

def score_game(random_predict)->int:
    """[summary]

    Args:
        random_predict ([type]): функция, выполняющая угадывание

    Returns:
        int: среднее кол-во попыток угадывания
    """
    
    count_ls=[] # список, хранящий кол-во попыток угадывания
    #np.random.seed(1)    # фиксируем последовательность случайных чисел, задав значение seed
    random_array = np.random.randint(1,501, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))  # определяем среднее кол-во попыток
    
    print(f"Ваш алгоритм угадывает число от 0 до 100 в среднем за {score} попыток")
    
    return score

if __name__ == '__main__':
    score_game(random_predict)