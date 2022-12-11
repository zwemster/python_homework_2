from random import randint

random_list = [randint(-10, 10) for i in range(int(input('Сколько чисел забить в список? ')))]
print(random_list)
summary = 0

for i in range(len(random_list)):
    if i % 2 != 0:
        summary += random_list[i]
print(f'Сумма элементов на нечётных позициях списка равна {summary}')
