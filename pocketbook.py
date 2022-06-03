# электронная книга, первое знакомство с tkinter
import tkinter as tk
import random
page = int(1)
win = tk.Tk()
win.title("Книга")
win.geometry("800x600")
res = tk.Label(win, text= 'Страница1')
res.place(x=700, y=20)
t = tk.Label(win, text='КАКОЙ ТО ТЕКСТ')
t.place(x=300, y=300)
def onclickf():
    global page
    x = random.randint(100,600)
    y = random.randint(100,600)
    page += 1
    res.configure(text='Страница {}'.format(page))
    t.place(x=x, y=y)
def onclickp():
    global page
    x = random.randint(100, 600)
    y = random.randint(100, 600)
    page -= 1
    res.configure(text='Страница {}'.format(page))
    t.place(x=x, y=y)
buttonF = tk.Button(win, text='След.стр', command = onclickf)
buttonF.place(x = 700, y=550)
buttonp = tk.Button(win, text='Пред.стр', command=onclickp)
buttonp.place(x=50, y=550)

win.mainloop()
