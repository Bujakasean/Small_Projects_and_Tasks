from random import randint, random
g = 100
c = 0
f = 0
while g >= 9:
    w = randint(0, 100)
    if w <= 50:
        c = c+1
        g = g-5
    elif w >= 50:
        g = g-3
        f = f+1
if g >= 5:
 print("Я разжег костер ", c, "раз, и ", f, "раз зафейлил. У меня осталась одна попытка, так как газа", g)
else: print("*выкинул зажигалку*")