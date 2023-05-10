# create boxes for word input as in wordle
# boxes are frames, named as box(ROW)(COLUMN)
# so, box11 ~ box55
# (you don't need the sixth row because you are dead at that point)
# item data structure, for each boxes:
# {'change':__, 'letter':__, 'selected':__, 'color':__}
# 'change': (bool) to be use in for loops, true execute function, false continue
# 'letter': (tk.StringVar()) what the character is
# 'selected': (bool) rendered as such, may have [last_selection_var] for fast deselection
# 'color': (str) gray, yellow, green

import tkinter as tk
from tkinter import ttk
import wordle_logic as wl

# class
class letter:
    selected = False
    color = 'gray'
    def __init__(self, box, ent, char, index):
        self.box = box
        self.ent = ent
        self.char = char
        self.index = index

    def __str__(self):
        return f'char:{self.char.get()} selected:{self.selected} color:{self.color}'

# func
def select(item):
    self = item.box
    if item.selected:
        #print('selected')
        cycle_color(item)
    else:
        #print('not selected')
        try:
            last_selected[0].box.configure(relief='')
            last_selected[0].selected = False
        except AttributeError:
            pass
        self.configure(relief=tk.GROOVE)
        last_selected.clear()
        last_selected.append(item)
        item.selected = True
    #print(item)

def cycle_color(item):
    self = item.box
    frame_style = self.configure()['style'][-1]
    if item.color == 'gray':
        self.configure(style='yellow.TFrame')
        item.ent.configure(bg='#B59F3A')
        item.color = 'yellow'
    elif item.color == 'yellow':
        self.configure(style='green.TFrame')
        item.ent.configure(bg='#528D4D')
        item.color = 'green'
    elif item.color == 'green':
        self.configure(style='gray.TFrame')
        item.ent.configure(bg='#3A3A3C')
        item.color = 'gray'
    else:
        raise Exception(f'cycle_color function broken from {item}')
    filter(item_tuple)

def write(char, move_to, select_to):
    try:
        char.set(char.get()[-1].upper())
        try:
            if char.get():
                move_to.focus_set()
                select(select_to)
        except AttributeError:
            pass
    except IndexError:
        pass
    filter(item_tuple)

def filter(items):
    poss_list_import = wl.possible_word_list.copy()
    poss_list.clear()
    poss_list.extend(wl.mass_filter(items, poss_list_import))
    table.delete(*table.get_children())
    lend = len(poss_list)
    modd = lend % 4
    for i in range(0, lend - modd, 4):
        data = (poss_list[i],
                poss_list[i + 1],
                poss_list[i + 2],
                poss_list[i + 3])
        table.insert(parent='', index=tk.END, values=data)
    if lend % 4 != 0:
        table.insert(parent='', index=tk.END, values=poss_list[modd * (-1):])

def reset():
    for item in item_tuple:
        select(item11)
        ent11.focus_set()
        item.char.set('')
        item.color = 'gray'
        item.box.configure(style='gray.TFrame')
        item.ent.configure(bg='#3A3A3C')

def delete_prev(item, prev):
    if not item.char.get():
        select(prev)
        prev.char.set('')
        prev.ent.focus_set()
        filter(item_tuple)

# window
window = tk.Tk()
window.geometry('400x700')
window.title('Wordle TryHard')
window.configure(bg = '#121214')
window.iconbitmap(r'icon.ico')

# style
style = ttk.Style()
style.theme_use('alt')
# style.configure('TFrame', background = 'white')
style.configure('TFrame', background='#3A3A3C')
style.configure('TButton', font=('BRHendrix-Regular', 10),
                background = '#3A3A3C',
                foreground = 'white',
                width = 7)
style.configure('black.TFrame', background='#121214')
style.configure('gray.TFrame', background='#3A3A3C')
style.configure('green.TFrame', background='#528D4D')
style.configure('yellow.TFrame', background='#B59F3A')
style.configure('Title.TLabel', background='#121214')
style.configure("Treeview", background='#121214',
                foreground='white',
                font=('BRHendrix-Regular', 10))
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
style.map('TButton', background=[('active','#3A3A3C')])

# variables
last_selected = ['starting value']
poss_list = []

# title
ttk.Label(
    master = window,
    text = 'Wordle TryHard',
    font = ('Franklin Gothic', '30'),
    background = '#121214',
    foreground = 'white'
    ).pack()

# frames
frame1 = ttk.Frame(window)
frame2 = ttk.Frame(window)
frame3 = ttk.Frame(window)
frame4 = ttk.Frame(window)
frame5 = ttk.Frame(window)

frame_tuple = (frame1, frame2, frame3, frame4, frame5)
for frame in frame_tuple:
    frame.configure(style = 'black.TFrame', width=355, height=71)
    frame.pack_propagate(False)
    frame.pack()

# boxes
box11 = ttk.Frame(frame1)
box12 = ttk.Frame(frame1)
box13 = ttk.Frame(frame1)
box14 = ttk.Frame(frame1)
box15 = ttk.Frame(frame1)

box21 = ttk.Frame(frame2)
box22 = ttk.Frame(frame2)
box23 = ttk.Frame(frame2)
box24 = ttk.Frame(frame2)
box25 = ttk.Frame(frame2)

box31 = ttk.Frame(frame3)
box32 = ttk.Frame(frame3)
box33 = ttk.Frame(frame3)
box34 = ttk.Frame(frame3)
box35 = ttk.Frame(frame3)

box41 = ttk.Frame(frame4)
box42 = ttk.Frame(frame4)
box43 = ttk.Frame(frame4)
box44 = ttk.Frame(frame4)
box45 = ttk.Frame(frame4)

box51 = ttk.Frame(frame5)
box52 = ttk.Frame(frame5)
box53 = ttk.Frame(frame5)
box54 = ttk.Frame(frame5)
box55 = ttk.Frame(frame5)

box_tuple = (box11, box12, box13, box14, box15,
           box21, box22, box23, box24, box25,
           box31, box32, box33, box34, box35,
           box41, box42, box43, box44, box45,
           box51, box52, box53, box54, box55)

for box in box_tuple:
    box.configure(width=65, height=65)
    box.pack_propagate(False)
    box.pack(side='left', padx=3)

# char
char11 = tk.StringVar()
char12 = tk.StringVar()
char13 = tk.StringVar()
char14 = tk.StringVar()
char15 = tk.StringVar()

char21 = tk.StringVar()
char22 = tk.StringVar()
char23 = tk.StringVar()
char24 = tk.StringVar()
char25 = tk.StringVar()

char31 = tk.StringVar()
char32 = tk.StringVar()
char33 = tk.StringVar()
char34 = tk.StringVar()
char35 = tk.StringVar()

char41 = tk.StringVar()
char42 = tk.StringVar()
char43 = tk.StringVar()
char44 = tk.StringVar()
char45 = tk.StringVar()

char51 = tk.StringVar()
char52 = tk.StringVar()
char53 = tk.StringVar()
char54 = tk.StringVar()
char55 = tk.StringVar()

# entry
ent11 = tk.Entry(box11, textvariable=char11)
ent12 = tk.Entry(box12, textvariable=char12)
ent13 = tk.Entry(box13, textvariable=char13)
ent14 = tk.Entry(box14, textvariable=char14)
ent15 = tk.Entry(box15, textvariable=char15)

ent21 = tk.Entry(box21, textvariable=char21)
ent22 = tk.Entry(box22, textvariable=char22)
ent23 = tk.Entry(box23, textvariable=char23)
ent24 = tk.Entry(box24, textvariable=char24)
ent25 = tk.Entry(box25, textvariable=char25)

ent31 = tk.Entry(box31, textvariable=char31)
ent32 = tk.Entry(box32, textvariable=char32)
ent33 = tk.Entry(box33, textvariable=char33)
ent34 = tk.Entry(box34, textvariable=char34)
ent35 = tk.Entry(box35, textvariable=char35)

ent41 = tk.Entry(box41, textvariable=char41)
ent42 = tk.Entry(box42, textvariable=char42)
ent43 = tk.Entry(box43, textvariable=char43)
ent44 = tk.Entry(box44, textvariable=char44)
ent45 = tk.Entry(box45, textvariable=char45)

ent51 = tk.Entry(box51, textvariable=char51)
ent52 = tk.Entry(box52, textvariable=char52)
ent53 = tk.Entry(box53, textvariable=char53)
ent54 = tk.Entry(box54, textvariable=char54)
ent55 = tk.Entry(box55, textvariable=char55)

ent_tuple = (ent11, ent12, ent13, ent14, ent15,
             ent21, ent22, ent23, ent24, ent25,
             ent31, ent32, ent33, ent34, ent35,
             ent41, ent42, ent43, ent44, ent45,
             ent51, ent52, ent53, ent54, ent55)

for ent in ent_tuple:
    ent.configure(justify='center',
                  bg='#3A3A3C',
                  fg='white',
                  width=2,
                  borderwidth=0,
                  font=('Franklin Gothic', 26),
                  insertbackground='white')
    ent.place(relx=0.5, rely=0.455, anchor='center')

# item
item11 = letter(box11, ent11, char11, 0)
item12 = letter(box12, ent12, char12, 1)
item13 = letter(box13, ent13, char13, 2)
item14 = letter(box14, ent14, char14, 3)
item15 = letter(box15, ent15, char15, 4)

item21 = letter(box21, ent21, char21, 0)
item22 = letter(box22, ent22, char22, 1)
item23 = letter(box23, ent23, char23, 2)
item24 = letter(box24, ent24, char24, 3)
item25 = letter(box25, ent25, char25, 4)

item31 = letter(box31, ent31, char31, 0)
item32 = letter(box32, ent32, char32, 1)
item33 = letter(box33, ent33, char33, 2)
item34 = letter(box34, ent34, char34, 3)
item35 = letter(box35, ent35, char35, 4)

item41 = letter(box41, ent41, char41, 0)
item42 = letter(box42, ent42, char42, 1)
item43 = letter(box43, ent43, char43, 2)
item44 = letter(box44, ent44, char44, 3)
item45 = letter(box45, ent45, char45, 4)

item51 = letter(box51, ent51, char51, 0)
item52 = letter(box52, ent52, char52, 1)
item53 = letter(box53, ent53, char53, 2)
item54 = letter(box54, ent54, char54, 3)
item55 = letter(box55, ent55, char55, 4)

item_tuple = (item11, item12, item13, item14, item15,
              item21, item22, item23, item24, item25,
              item31, item32, item33, item34, item35,
              item41, item42, item43, item44, item45,
              item51, item52, item53, item54, item55)

# event
    # box selection
box11.bind('<Button>', lambda event: select(item11))
box12.bind('<Button>', lambda event: select(item12))
box13.bind('<Button>', lambda event: select(item13))
box14.bind('<Button>', lambda event: select(item14))
box15.bind('<Button>', lambda event: select(item15))

box21.bind('<Button>', lambda event: select(item21))
box22.bind('<Button>', lambda event: select(item22))
box23.bind('<Button>', lambda event: select(item23))
box24.bind('<Button>', lambda event: select(item24))
box25.bind('<Button>', lambda event: select(item25))

box31.bind('<Button>', lambda event: select(item31))
box32.bind('<Button>', lambda event: select(item32))
box33.bind('<Button>', lambda event: select(item33))
box34.bind('<Button>', lambda event: select(item34))
box35.bind('<Button>', lambda event: select(item35))

box41.bind('<Button>', lambda event: select(item41))
box42.bind('<Button>', lambda event: select(item42))
box43.bind('<Button>', lambda event: select(item43))
box44.bind('<Button>', lambda event: select(item44))
box45.bind('<Button>', lambda event: select(item45))

box51.bind('<Button>', lambda event: select(item51))
box52.bind('<Button>', lambda event: select(item52))
box53.bind('<Button>', lambda event: select(item53))
box54.bind('<Button>', lambda event: select(item54))
box55.bind('<Button>', lambda event: select(item55))

    # entry selection
ent11.bind('<Button>', lambda event: select(item11))
ent12.bind('<Button>', lambda event: select(item12))
ent13.bind('<Button>', lambda event: select(item13))
ent14.bind('<Button>', lambda event: select(item14))
ent15.bind('<Button>', lambda event: select(item15))

ent21.bind('<Button>', lambda event: select(item21))
ent22.bind('<Button>', lambda event: select(item22))
ent23.bind('<Button>', lambda event: select(item23))
ent24.bind('<Button>', lambda event: select(item24))
ent25.bind('<Button>', lambda event: select(item25))

ent31.bind('<Button>', lambda event: select(item31))
ent32.bind('<Button>', lambda event: select(item32))
ent33.bind('<Button>', lambda event: select(item33))
ent34.bind('<Button>', lambda event: select(item34))
ent35.bind('<Button>', lambda event: select(item35))

ent41.bind('<Button>', lambda event: select(item41))
ent42.bind('<Button>', lambda event: select(item42))
ent43.bind('<Button>', lambda event: select(item43))
ent44.bind('<Button>', lambda event: select(item44))
ent45.bind('<Button>', lambda event: select(item45))

ent51.bind('<Button>', lambda event: select(item51))
ent52.bind('<Button>', lambda event: select(item52))
ent53.bind('<Button>', lambda event: select(item53))
ent54.bind('<Button>', lambda event: select(item54))
ent55.bind('<Button>', lambda event: select(item55))

    # backspace
ent12.bind('<BackSpace>', lambda event: delete_prev(item12, item11))
ent13.bind('<BackSpace>', lambda event: delete_prev(item13, item12))
ent14.bind('<BackSpace>', lambda event: delete_prev(item14, item13))
ent15.bind('<BackSpace>', lambda event: delete_prev(item15, item14))
ent21.bind('<BackSpace>', lambda event: delete_prev(item21, item15))
ent22.bind('<BackSpace>', lambda event: delete_prev(item22, item21))
ent23.bind('<BackSpace>', lambda event: delete_prev(item23, item22))
ent24.bind('<BackSpace>', lambda event: delete_prev(item24, item23))
ent25.bind('<BackSpace>', lambda event: delete_prev(item25, item24))
ent31.bind('<BackSpace>', lambda event: delete_prev(item31, item25))
ent32.bind('<BackSpace>', lambda event: delete_prev(item32, item31))
ent33.bind('<BackSpace>', lambda event: delete_prev(item33, item32))
ent34.bind('<BackSpace>', lambda event: delete_prev(item34, item33))
ent35.bind('<BackSpace>', lambda event: delete_prev(item35, item34))
ent41.bind('<BackSpace>', lambda event: delete_prev(item41, item35))
ent42.bind('<BackSpace>', lambda event: delete_prev(item42, item41))
ent43.bind('<BackSpace>', lambda event: delete_prev(item43, item42))
ent44.bind('<BackSpace>', lambda event: delete_prev(item44, item43))
ent45.bind('<BackSpace>', lambda event: delete_prev(item45, item44))
ent51.bind('<BackSpace>', lambda event: delete_prev(item51, item45))
ent52.bind('<BackSpace>', lambda event: delete_prev(item52, item51))
ent53.bind('<BackSpace>', lambda event: delete_prev(item53, item52))
ent54.bind('<BackSpace>', lambda event: delete_prev(item54, item53))
ent55.bind('<BackSpace>', lambda event: delete_prev(item55, item54))

# trace
item11.char.trace("w", lambda char, move_to, not_used: (write(item11.char, ent12, item12)))
item12.char.trace("w", lambda char, move_to, not_used: (write(item12.char, ent13, item13)))
item13.char.trace("w", lambda char, move_to, not_used: (write(item13.char, ent14, item14)))
item14.char.trace("w", lambda char, move_to, not_used: (write(item14.char, ent15, item15)))
item15.char.trace("w", lambda char, move_to, not_used: (write(item15.char, ent21, item21)))

item21.char.trace("w", lambda char, move_to, not_used: (write(item21.char, ent22, item22)))
item22.char.trace("w", lambda char, move_to, not_used: (write(item22.char, ent23, item23)))
item23.char.trace("w", lambda char, move_to, not_used: (write(item23.char, ent24, item24)))
item24.char.trace("w", lambda char, move_to, not_used: (write(item24.char, ent25, item25)))
item25.char.trace("w", lambda char, move_to, not_used: (write(item25.char, ent31, item31)))

item31.char.trace("w", lambda char, move_to, not_used: (write(item31.char, ent32, item32)))
item32.char.trace("w", lambda char, move_to, not_used: (write(item32.char, ent33, item33)))
item33.char.trace("w", lambda char, move_to, not_used: (write(item33.char, ent34, item34)))
item34.char.trace("w", lambda char, move_to, not_used: (write(item34.char, ent35, item35)))
item35.char.trace("w", lambda char, move_to, not_used: (write(item35.char, ent41, item41)))

item41.char.trace("w", lambda char, move_to, not_used: (write(item41.char, ent42, item42)))
item42.char.trace("w", lambda char, move_to, not_used: (write(item42.char, ent43, item43)))
item43.char.trace("w", lambda char, move_to, not_used: (write(item43.char, ent44, item44)))
item44.char.trace("w", lambda char, move_to, not_used: (write(item44.char, ent45, item45)))
item45.char.trace("w", lambda char, move_to, not_used: (write(item45.char, ent51, item51)))

item51.char.trace("w", lambda char, move_to, not_used: (write(item51.char, ent52, item52)))
item52.char.trace("w", lambda char, move_to, not_used: (write(item52.char, ent53, item53)))
item53.char.trace("w", lambda char, move_to, not_used: (write(item53.char, ent54, item54)))
item54.char.trace("w", lambda char, move_to, not_used: (write(item54.char, ent55, item55)))
item55.char.trace("w", lambda char, move_to, not_used: (write(item55.char, None, None)))

select(item11)
ent11.focus_set()

# reset
ttk.Button(window, text = 'RESET', command = reset).pack(pady = 15)
window.bind('<Control-BackSpace>', lambda event: reset())

# table
columns = ('col1', 'col2', 'col3', 'col4', 'col_useless_fuxk')
table = ttk.Treeview(window,
                     columns = columns,
                     show = 'tree')
table.column("#0", width=0)
for column in columns[:-1]:
    table.heading(column, text = '')
    table.column(column = column, width=80)
table.column("col_useless_fuxk", width=10)
table.pack(pady = 5)



# run
window.mainloop()
