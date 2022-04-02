# **Проект 0. Угадай число**

## **Оглавление**
[1. Описание проекта](https://github.com/kostritsky/sf_data_science/tree/main/project_0/README.md#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/kostritsky/sf_data_science/tree/main/project_0/README.md#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/kostritsky/sf_data_science/tree/main/project_0/README.md#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/kostritsky/sf_data_science/tree/main/project_0/README.md#Этапы-работы-над-проектом)

[5. Результат](https://github.com/kostritsky/sf_data_science/tree/main/project_0/README.md#Результат)

[6. Выводы](https://github.com/kostritsky/sf_data_science/tree/main/project_0/README.md#Выводы)

### **Описание проекта**
Необходимо разработать алгоритм, позволяющий угадать загаданное компьютером целое число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/kostritsky/sf_data_science/tree/main/project_0/README.md#Оглавление)

**Условия соревнования**
- Компьютер загадывает целое число от n до m, где n, m - натуральные целые числ (причем m>n), а разработанный алгоритм его "угадывает". 
- Алгоритм может учитывать информацию о том, больше или меньше предполагаемое число загаданному компьютером.

**Метрика качества**

Результаты оцениваются по среднему количеству попыток при 1000 повторений.

**Что практикуем**

Учимся писать хороший код на Python.

### **Краткая информация о данных**
.....

### **Этапы работы над проектом**


1. Вносим изменения в алгоритм загадывания чисел, позволяя указывать произвольный интервал для загадывания.

2. Разрабатываем и реализуем алгоритм угадывания. Дорабатываем процедуру определения среднего кол-ва попыток угадывания для произвольного интервала загаданного числа.

3. Отлаживаем работу процедур в debugger

4. Определяем среднее кол-во попыток для интервала от 1 до 100.Определяем максимальную величину интервала, при котором среднее число попыток будет меньше 20.

5. Готовим презентацию результатов в виде Jupyther Notebook. 

6. Определяем условия для воспроизводимости кода: переносим версии использованных библиотек и полную информацию об окружении в отдельные файлы и размещаем их в папке с проектом.

7. Вносим описание проекта в файл README.md, фиксируем все изменения в файлах проекта. Размещаем проект на GitHUB.

### **Результат**

Для угадывания числа использован алгоритм, предполагаючий, что загаданное число является средним интервала угаданным чисел. Если загаданное число меньше среднего по интервалу, на следующем шаге максимальное значение интервала загаданного числа приравнивается среднему значению интервала с предыдущего шага. Если загаданное число больше среднего по интервалу, минимальное значение интервала на следующем шаге меняется на среднее из текущего шага.

Данный алгоритм позволяет угадать число для интервала от 1 до 100 в среднем за 5 попыток. 

Экспериментально показано, что максимальный интервал загаданных чисел, для которого среднее число попыток будет меньше 20, равен 1000000.

### **Вывод**
 Предлагаемый алгоритм позволяет решить поставленную задачу -- "угадать" число за минимальное кол-во попыток.





:arrow_up:[к оглавлению](https://github.com/kostritsky/sf_data_science/tree/main/project_0/README.md#Оглавление)