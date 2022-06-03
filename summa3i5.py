obsh = int(input('Введите число '))
summa = int()
for i in range(1, obsh):
    if i % 3 == 0:
        summa = summa + i
    elif i % 5 == 0:
        summa = summa + i
print('Общая сумма = {}'.format(summa))


