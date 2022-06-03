import random
number = random.randint(0, 100)
running = True
schet = int()
mnogo = int()
while running:
    if schet != 5:
        schet = schet + 1
        guess = int(input('Введите целое число : '))
        if guess == number:
            print('Поздравляю, вы угадали.')
            running = False
        elif guess < number:
            mnogo = number - guess
            if mnogo >= 10:
                print('Нет, загаданное число НАмного больше этого.')
            else:
                print('Нет, загаданное число немного больше этого.')
        else:
             mnogo = guess - number
             if mnogo >= 10:
                 print('Нет, загаданное число НАмного меньше этого.')
             else:
                print('Нет, загаданное число немного меньше этого.')
    else:
        break
else:
    print('Цикл while закончен.')
if running == True:
    print('Ты обложался')
print('Завершение.')
