#!/usr/bin/env python3

"""Botoes de seleção, checkButtons  e radioButtons"""

from tkinter import *
from tkinter import ttk

root = Tk()
checkButton = ttk.Checkbutton(root, text='SPAM?')
checkButton.pack()

# passando uma string
spam = StringVar()
#spam.set('SPAM!')

checkButton.config(variable=spam, onvalue='SPAM checked!', offvalue='SPAM Not checked!')
print(spam.get())

# Inserindo radioButtons
breakfast = StringVar()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()
ttk.Radiobutton(root, text='EGGS', variable=breakfast, value='EGGS').pack()
ttk.Radiobutton(root, text='SAUSAGE', variable=breakfast, value='SAUSAGE').pack()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()

#print(breakfast.get())

# Por ultimo vamos alterar o comportamento do nosso checkButton
# ao selecionar o radioButton vamos alterar o nome do checkButton
#checkButton.config(textvariable=breakfast)

root.mainloop()
