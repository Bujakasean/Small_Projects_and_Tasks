#начиная с 10 находит в общем все числа которые делятся на N или его содержат
n = int(input('N'))
x = int(input('общее'))
chisla = []
for i in range(10, x + 1):
    if i % n == 0:
        chisla.append(i)
    else:
        a = i % 10
        if a == n:
            chisla.append(i)
        else:
            b = i - a
            b = b // 10
            if b == n:
                chisla.append(i)
print(chisla)
