summary = 0
array = list(map(int, input('Введи сколь угодно чисел: ').split()))
for i in range(len(array)):
    if i % 2 != 0:
        summary += array[i]
print(f'Сумма элементов на нечётных позициях {summary}')