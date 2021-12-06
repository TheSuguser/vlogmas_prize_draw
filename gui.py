from io import StringIO
from os import replace
from tkinter import *
import time

import numpy as np

from utils import *

candidates = load_data('data')
cs = ["", "", ""]


def show_member(pool: StringVar):
    global candidates
    c = np.random.choice(candidates, size=1)
    pool.set(c[0])

    window.after(100, show_member, pool)
    return

def draw(c1,c2,c3):
    global cs
    _c = np.random.choice(candidates, size=1, replace=True)
    if len(cs)<3:
        cs =  list(_c) + cs
    else:
        cs.pop(-1)
        cs =  list(_c) + cs
    
    c1.set(cs[0])
    c2.set(cs[1])
    c3.set(cs[2])
    return 

def draw2(winner):
    _c = np.random.choice(cs, size=1)
    winner.set(_c[0])
    return


if __name__ == "__main__":
    window = Tk(screenName='VLOGMAS Prize Draw')

    # Basic Layout
    window.geometry("500x700")
    window.title("VLOGMAS Prize Draw")

    # First Round Frame
    frame1 = Frame(
        window,
        relief=RAISED, 
        borderwidth=2,
        width=400,
        height=300,)
    frame1.pack(side=TOP, fill=BOTH,ipadx=5, ipady=5, expand=True)
    # Candidate Pool Label
    pool = StringVar(value="name")
    pool_label = Label(
        frame1,
        textvariable=pool,
        font=20,
        justify="center",
        bg='#e0c8d1'
        )
    pool_label.place(x=60, y=10, width=380, height=150)

    show_member(pool)

    c1 = StringVar(value="")
    c2 = StringVar(value="")
    c3 = StringVar(value="")


    # First Draw Button
    button1 = Button(
        frame1, 
        text="第一轮",
        justify='center',
        command=lambda:draw(c1,c2,c3)
    )
    button1.place(width=80, height=40, x=360 , y=170, )

    # Second Round Pool Label
    frame2 = Frame(
        window,
        relief=RAISED, 
        borderwidth=2,
        width=400,
        height=200)
    frame2.pack(fill=BOTH, ipadx=5, ipady=5, expand=True)
    
    c1label = Label(
        frame2, 
        textvariable=c1, 
        font=10,
        justify='center',
        bg='#e0c8d1'
    )
    c1label.place(x=60, y=10, width=100, height=50)

    c2label = Label(
        frame2, 
        textvariable=c2, 
        font=10,
        justify='center',
        bg='#e0c8d1'
    )
    c2label.place(x=200, y=10, width=100, height=50)

    c3label = Label(
        frame2, 
        textvariable=c3, 
        font=10,
        justify='center',
        bg='#e0c8d1'
    )
    c3label.place(x=340, y=10, width=100, height=50)


    # Second Draw Button
    winner = StringVar(value="")
    button2 = Button(
        frame2, 
        text="第二轮",
        justify='center',
        command=lambda:draw2(winner)
    )
    button2.place(width=80, height=40, x=360 , y=120, )

    # Final Winner Label
    frame3 = Frame(
        window,
        relief=RAISED, 
        borderwidth=2,
        width=400,
        height=100,
        bg='#000000')
    frame3.pack(fill=BOTH, ipadx=5, ipady=5, expand=True)

    wlabel = Label(
        frame3, 
        textvariable=winner, 
        font=20,
        justify='center',
        bg='#e0c8d1'
    )
    wlabel.place(x=60, y=10, width=380, height=100)
    window.mainloop()