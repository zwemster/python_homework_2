array = list(map(int, input('Введи сколько хочешь чисел через пробел: ').split()))
mult = 0
print(f'Исходный массив: {array}')
for i in range(int(len(array) / 2)):
    mult = array[i] * array[len(array) - i - 1]
    print(f'Произведение {i + 1} пары равно {mult}')
if len(array) % 2 == 1:
    print(f'Произведение последней пары  {array[int(len(array) / 2)] ** 2} ')