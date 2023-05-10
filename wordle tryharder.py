import tkinter as tk
from tkinter import ttk
import wordle_logic as wl

def search(word):
    if str(word) in wl.possible_word_list:
        entry.configure(bg='#22ab3e')
    else:
        entry.configure(bg='#ab2222')

def write(text, _, __):
    if len(text.get()) <= 5:
        text.set(text.get().upper())
        entry.configure(bg='#3A3A3C')
        if len(text.get()) == 5:
            search(text.get())
    else:
        text.set(text.get()[:5])

# window
window = tk.Tk()
window.geometry('400x160')
window.title('Wordle TryHarder')
window.configure(bg = '#121214')
window.iconbitmap(r'icon.ico')

# title
ttk.Label(
    master = window,
    text = 'Wordle TryHarder',
    font = ('Franklin Gothic', '30'),
    background = '#121214',
    foreground = 'white'
    ).place(relx=0.5, y = 50, anchor='center')

# variable
text = tk.StringVar()

# entry
entry = tk.Entry(window,
                 textvariable = text,
                 justify='center',
                 bg='#3A3A3C',
                 fg='white',
                 width=6,
                 borderwidth=0,
                 font=('Franklin Gothic', 20),
                 insertbackground='white'
                 )
entry.place(relx=0.5, y = 100, anchor='center')

# event
entry.bind('<Control-BackSpace>', lambda event: text.set(''))
text.trace("w", lambda char, _, __: (write(text, None, None)))

# run
window.mainloop()