import random
import time
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
DealerChips = 1000
PlayerChips = 1000
ingame = True
DealerHand = int()
PlayerHand = int()
stack = int()
newdeck = deck


def dealerstack():
    global DealerHand
    while DealerHand < 16:
        card = random.choice(deck)
        deck.remove(card)
        DealerHand += card
        print('Диллер получил {}'.format(card))
        print('Карты диллера равны {}'.format(DealerHand))
        print()
        time.sleep(1)
    if DealerHand > 21:
        print('Перебор')
        print()
        DealerHand = 0

    if DealerHand != 0:
        playerstack()


def playerstack():
    global PlayerHand
    choise = str
    card = random.choice(deck)
    deck.remove(card)
    print('Вам выдали {}'.format(card))
    PlayerHand += card
    print('Сумма Ваших карт равна {}'.format(PlayerHand))
    print()
    time.sleep(1)
    while choise != '-':
        card = random.choice(deck)
        deck.remove(card)
        print('Вам выдали {}'.format(card))
        PlayerHand += card
        if PlayerHand > 21:
            print('Перебор!')
            PlayerHand = 0
            break
        print('Сумма Ваших карт равна {}'.format(PlayerHand))
        print()
        choise = input('Еще?')
        time.sleep(1)


def bets():
    global PlayerChips
    global DealerChips
    global stack
    bet = int(input('Сделайте вашу ставку '))
    stack = bet * 2
    print('Банк составляет {}'.format(stack))
    print()
    PlayerChips -= bet
    DealerChips -= bet


def win():
    global PlayerChips
    global DealerHand
    global DealerChips
    global PlayerHand
    global deck
    if DealerHand == 0:
        PlayerHand = 1
    if PlayerHand > DealerHand:
        print('Вы выиграли {} фишек'.format(stack))
        print()
        PlayerChips += stack
    if PlayerHand == DealerHand:
        print('НИЧЬЯ!')
        PlayerChips += stack // 2
        DealerChips += stack // 2
    if DealerHand > PlayerHand:
        DealerChips += stack
    PlayerHand = 0
    DealerHand = 0
    deck = newdeck.copy()


while ingame:
    if DealerChips == 0:
        ingame = False
        print('Поздравляю вы выиграли все фишки')
        continue
    elif PlayerChips == 0:
        ingame = False
        print('Вы проиграли все фишки')
        continue
    if {str(PlayerChips)[len(str(PlayerChips))-1]} == '1':
        print('У Вас {} фишка'.format(PlayerChips))
    elif {str(PlayerChips)[len(str(PlayerChips))-1]} in ['2', '3', '4']:
        print('У Вас {} фишки'.format(PlayerChips))
    else:
        print('У Вас {} фишек'.format(PlayerChips))
    print(len(deck))
    bets()
    dealerstack()
    win()
