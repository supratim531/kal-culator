import tkinter as t

win = t.Tk()
win.maxsize(350, 370)
win.geometry('350x370')
win.title('Calculator')

btnwid = 4
btnhig = 10

value = t.StringVar()
value.set('')

screen = t.Entry(win, textvar=value, font='lucida 35 bold')
screen.pack(fill=t.X, padx=5, pady=20)

def click(e):
    global value
    character = e.widget.cget('text')
    print(character)
    if character == 'X':
        value.set(value.get() + '*')
        screen.update()
        return
    if character == '=':
        if value.get().isdigit():
            character = int(value.get())
        else:
            character = eval(value.get())
        value.set(character)
        screen.update()
    elif character == 'C':
        value.set('')
        screen.update()
    else:
        value.set(value.get() + character)
        screen.update()
    pass

f = t.Frame(win, bg='grey')
f.pack(side=t.TOP, anchor='w')

b = t.Button(f, text='9', width=btnwid, font='lucida 18 bold', bg='orange', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f, text='8', width=btnwid, font='lucida 18 bold', bg='orange', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f, text='7', width=btnwid, font='lucida 18 bold', bg='orange', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f, text='+', width=btnwid, font='lucida 18 bold', bg='red', fg='white', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

# =============================================================

f1 = t.Frame(win, bg='grey')
f1.pack(side=t.TOP, anchor='w', pady=5)

b = t.Button(f1, text='6', width=btnwid, font='lucida 18 bold', bg='orange', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f1, text='5', width=btnwid, font='lucida 18 bold', bg='orange', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f1, text='4', width=btnwid, font='lucida 18 bold', bg='orange', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f1, text='-', width=btnwid, font='lucida 18 bold', bg='red', fg='white', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

# =============================================================

f2 = t.Frame(win, bg='grey')
f2.pack(side=t.TOP, anchor='w', pady=5)

b = t.Button(f2, text='3', width=btnwid, font='lucida 18 bold', bg='orange', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f2, text='2', width=btnwid, font='lucida 18 bold', bg='orange', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f2, text='1', width=btnwid, font='lucida 18 bold', bg='orange', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f2, text='/', width=btnwid, font='lucida 18 bold', bg='red', fg='white', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

# =============================================================

f3 = t.Frame(win, bg='grey')
f3.pack(side=t.TOP, anchor='w', pady=5)

b = t.Button(f3, text='C', width=btnwid, font='lucida 18 bold', bg='dark grey', fg='white', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f3, text='0', width=btnwid, font='lucida 18 bold', bg='orange', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f3, text='X', width=btnwid, font='lucida 18 bold', bg='red', fg='white', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

b = t.Button(f3, text='=', width=btnwid, font='lucida 18 bold', bg='blue', fg='white', border=5)
b.pack(side=t.LEFT, padx=5)
b.bind('<Button-1>', click)

# =============================================================

win.mainloop()