# -*- coding: utf-8 -*-

__author__ = 'MaoWei'

__date__ = '2017/10/25'


from Tkinter import *
import random

time1 = 0
time2 = 0
time3 = 0
time4 = 0
time5 = 0
time6 = 0
list_content = []

def xin1():
  global c1,time1
  if time1 % 2 == 0:
    time1 += 1
    list_content.append('一食堂')
  else:
    time1 += 1
    list_content.remove('一食堂')

def xin2():
  global c2,time2
  if time2 % 2 == 0:
    time2 += 1
    list_content.append('二食堂')
  else:
    time2 += 1
    list_content.remove('二食堂')

def xin3():
  global c3,time3
  if time3 % 2 == 0:
    time3 += 1
    list_content.append('四食堂')
  else:
    time3 += 1
    list_content.remove('四食堂')

def xin4():
  global c4,time4
  if time4 % 2 == 0:
    time4 += 1
    list_content.append('小观园')
  else:
    time4 += 1
    list_content.remove('小观园')

def xin5():
  global c5,time5
  if time5 % 2 == 0:
    time5 += 1
    list_content.append('菜市场')
  else:
    time5 += 1
    list_content.remove('菜市场')

def xin6():
  global c6,time6
  if time6 % 2 == 0:
    time6 += 1
    list_content.append('孙对请客')
  else:
    time6 += 1
    list_content.remove('孙对请客')

def choose():
  L = Label(root,text = random.sample(list_content,1),font = 60,fg = 'red',width = 20).grid(row = 1,column = 2,rowspan = 3,sticky = S)

root = Tk()
root.title("今天吃什么")
root.geometry('400x200')
c1 = Checkbutton(root,text = "一食堂 ",command = xin1,font = 40,width = 20).grid(row = 0,column = 1,sticky = E+W)
c2 = Checkbutton(root,text = "二食堂 ",command = xin2,font = 40,width = 20).grid(row = 1,column = 1,sticky = E+W)
c3 = Checkbutton(root,text = "四食堂 ",command = xin3,font = 40,width = 20).grid(row = 2,column = 1,sticky = E+W)
c4 = Checkbutton(root,text = "小观园 ",command = xin4,font = 40,width = 20).grid(row = 3,column = 1,sticky = E+W)
c5 = Checkbutton(root,text = "菜市场 ",command = xin5,font = 40,width = 20).grid(row = 4,column = 1,sticky = E+W)
c6 = Checkbutton(root,text = "孙对请客",command = xin6,font = 40,width = 20).grid(row = 5,column = 1,sticky = E+W)

L = Button(root,text = "开始选择",command = choose,font = 50,width = 20).grid(row = 0,column = 2,rowspan = 3,sticky = E+W)

root.mainloop()
