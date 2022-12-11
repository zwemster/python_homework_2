fibonacci = [0, 1]
negative = []
size = int(input('Сколько чисел Фибоначчи ты хочешь видеть? '))
if size > 1:
    for i in range(2, size):
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

    for i in range(2, size):
        negative.append(((fibonacci[i-2]) + (fibonacci[i-1])) * (-1)**(i-1))
    negative = list(reversed(negative))
else:
    print(f'[{fibonacci[0]}]')
negative.extend(fibonacci)
print(negative)