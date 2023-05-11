from tkinter import *
import time
import random

win = Tk()
win.geometry('560x480')
win.resizable(0,0)
win.title('Rock Paper Scissor')
win.configure(background='#aaaaff')

Score = 0
result = ['Play Again', 'Computer Won!', 'You Won!']
my_img = ['stone.png','paper.png','scissor.png']
opening_img = 'smil.png'

def reset():
    img = PhotoImage(file=opening_img)
    canva1.config(image=img)
    canva1.image=img
    canva2.config(image=img)
    canva2.image=img
    score.config(text='Score: 0',font=('comic sans ms', 18))
    
    print('Reset Done!')
def show(var,x,c):
    global Score
    my_text = result[var]
    x=int(x)
    c=int(c)
    print(my_text)
    update.config(text=my_text,font=('comic sans ms', 18))
    if my_text == result[2]:
        Score=Score+1
        ans = 'Score: '+str(Score)
        score.config(text=ans,font=('comic sans ms', 16))
    im1 = PhotoImage(file=my_img[x])
    canva1.config(image=im1)
    canva1.image=im1
    img2 = PhotoImage(file=my_img[c])
    canva2.config(image=img2)
    canva2.image=img2
    
def rock():
    x = 0
    c = random.randint(0,2)
    print(c)
    if x==c:
        print(result[0])
        show(0,x,c)
    elif c==1:
        print(result[1])
        show(1,x,c)
    else:
        print(result[2])
        show(2,x,c)

def paper():
    x = 1
    c = random.randint(0,2)
    print(c)
    if c == 0:
        print(result[2])
        show(2,x,c)
    elif x==c:
        print(result[0])
        show(0,x,c)
    else:
        print(result[1])
        show(1,x,c)

def scissor():
    x = 2
    c = random.randint(0,2)
    print(c)
    if c == 0:
        print(result[1])
        show(1,x,c)
    elif c == 1:
        print(result[2])
        show(2,x,c)
    else:
        print(result[0])
        show(0,x,c)

heading = Label(win, text='Rock Paper Scissor',
                font=('comic sans ms', 24,'bold','underline'),background='#aaaaff')
heading.grid(row=0,column=0,pady=10,padx=10,columnspan =3)

my_text='Welcome to Rock,\nPaper, Scissor game\nYou are playing\nwith computer'
update = Label(win, text=my_text,background='#aaaaff',
               height=5,width=16,font=('comic sans ms', 18))
update.grid(row=2,column=1)
                     
note = Label(win, text='Click the button at the top of your choise',
             background='#aaaaff',font=('comic sans ms', 14))
note.grid(row=3,column=0,columnspan =3)

score = Label(win, text='Score: 0',background='#aaaaff',font=('comic sans ms', 16))
score.grid(row=4,column=0,columnspan =3)

img_open = PhotoImage(file= opening_img)
canva1 = Label(win,image=img_open,background='#aaaaff')
canva1.grid(row=2,column=0)

canva2 = Label(win,image=img_open,background='#aaaaff')
canva2.grid(row=2,column=2)

rock_b = Button(win, text="Rock",font=('comic sans ms',14,'bold'),height=3,width=8,
                   activebackground='#55cc55',bg='#00ff00',
                borderwidth = 3,command=rock).grid(row=1,column=0,padx=10)
paper_b = Button(win, text="Paper",font=('comic sans ms',14,'bold'),height=3,width=8,
                   activebackground='#5555cc',bg='#0000ff', borderwidth = 3,
                 command=paper).grid(row=1,column=1,padx=10)
scissor_b = Button(win, text="Scissor",font=('comic sans ms',14,'bold'),height=3,width=8,
                   activebackground='#cc5555',bg='#ff0000',borderwidth = 3,
                   command=scissor).grid(row=1,column=2,padx=10)
clear_b = Button(win,text='Reset',font=('comic sans ms',12),height=1,width=8,
                   activebackground='#eeeeee',bg='#aaaaaa',command=reset).grid(row=5,column=1,pady=10)

win.mainloop()
