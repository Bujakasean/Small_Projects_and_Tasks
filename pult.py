# пульт от телевизора
current_channel = int(1)
volume = int(1)
on_off = True
def screen():
    if 0 < current_channel <= 5:
        print('{}{}'.format(current_channel, volume))
    if 5 < current_channel <= 10:
        print('{}{}'.format(current_channel, volume))
screen()
while on_off:
    update = input()
    try:
        update = int(update)
    except:
        None
    if update == 'off':
        print('Выключение')
        break
    elif update == 'n':
        if current_channel == 10:
            current_channel = 1
            screen()
        else:
            current_channel = current_channel + 1
            screen()
    elif update == 'p':
        if current_channel <= 1:
            current_channel = 11
        current_channel = current_channel - 1
        screen()
    elif update == '+':
        if volume == 10:
            screen()
        else:
            volume = volume + 1
            screen()
    elif update == '-':
        if volume == 1:
            screen()
        else:
            volume = volume - 1
            screen()
    elif update <= 10:
        current_channel = update
        screen()









