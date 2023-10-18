# -*- coding: utf-8 -*-

__author__ = 'MaoWei'
__date__ = '2017/10/25'
__version__ = 'V1.0'

from tkinter import *
import random

list_content = ['一食堂', '二食堂', '四食堂', '小观园', '菜市场', '孙对请客']

def toggle_food(food):
    if food in list_content:
        list_content.remove(food)
    else:
        list_content.append(food)

def choose():
    if list_content:
        chosen_food = random.choice(list_content)
        label.config(text=chosen_food, fg='red')
    else:
        label.config(text='没有可选的食堂', fg='black')

root = Tk()
root.title("今天吃什么")
root.geometry('400x200')

for i, food in enumerate(list_content):
    check_button = Checkbutton(root, text=food, command=lambda f=food: toggle_food(f), font=40, width=20)
    check_button.grid(row=i, column=1, sticky=E+W)

choose_button = Button(root, text="开始选择", command=choose, font=50, width=20)
choose_button.grid(row=0, column=2, rowspan=len(list_content), sticky=E+W)

label = Label(root, text="", font=60, fg='red', width=20)
label.grid(row=0, column=3, rowspan=len(list_content), sticky=S)

root.mainloop()
