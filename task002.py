array = list(map(float, input('Введи сколько хочешь десятичных дробей через пробел: ').split()))
print(f'Исходный массив: {array}')
for i in range(len(array)):
    array[i] = round((array[i] % 1), 3)
diff = max(array) - min(array)
print(f'Разница между максимальным и минимальным значением дробной части равна {diff}')