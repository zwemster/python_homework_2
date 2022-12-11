number = int(input('Введи обычное число: '))
binary = ''
while number > 0:
    binary = str(number % 2) + binary
    number //= 2
print(binary)