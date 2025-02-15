from tkinter import*
import time
from math import*
from random import*
ara=Tk()
ara.geometry("1024x1824")
ara.title("Zachet Markos")
can=Canvas(ara,width=1024,height=633,bg="turquoise")
import random
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet","pink","black","brown"]
can.pack()

##поле ввода
vk=StringVar()
ak=StringVar()
pola=Entry(textvariable=ak)
polv=Entry(textvariable=vk)
pola.place(x=780,y=1220,anchor="w")
polv.place(x=780,y=1140,anchor="w")
global counter
counter=0
global coounter
coounter=0

##защита от дурака
def tea(e):
    global coounter
    if e.keysym=="1" or e.keysym=="2" or e.keysym=="3" or e.keysym=="4" or e.keysym=="5" or e.keysym=="6" or e.keysym=="7" or e.keysym=="8" or e.keysym=="9" or e.keysym=="0":
            coounter+=1
    elif e.keysym=="BackSpace" and coounter!=0:
        coounter-=1
    else: 
         polv.delete (coounter,END)
polv.bind("<KeyRelease>",tea)

##функция для анимации
def plane():
    can.delete("boom")
    ara.unbind("<Button-1>")
    t=0
    y0=525
    y1=700
    y2=560
    g=9.8
    S=int(vk.get())
    while 1==1:
        V0=70
        V2=-28
        t=t+0.025
        x1=V0*t
        x2=S+V2*t
        x3=S+V2*t+2
        x4=S+V2*t+27
        x5=V0*t+60
        y1=y0+g*(t**2)/2
        a=can.create_rectangle(x1,10,x1+60,60,fill="red")
        f=can.create_line(x5,10,x5+60,35,fill="red",width=4)
        h=can.create_line(x5,60,x5+60,35,fill="red",width=4)
        b=can.create_oval(x1,y1-500,x1+30,y1-470,fill="black")
        c=can.create_rectangle(x2,y0,x2+45,y0+45,fill="purple")
        d=can.create_oval(x3,y2,x3+17,y2+17,fill="brown")
        e=can.create_oval(x4,y2,x4+17,y2+17,fill="brown")
        ara.update()
        time.sleep(0.01)
        can.delete(a)
        can.delete(b)
        can.delete(c)
        can.delete(d)
        can.delete(e)
        can.delete(f)
        can.delete(h)
        if x1+30>x2 and x1<x2+45 and y1-500+30>y0 and y1-500<y0+45: 
            can.delete(b)
            e=can.create_oval(830,600,630,400,fill=random.choice(colors),outline="red",tag="boom")
            I=can.create_text(712,300,text="HIT",font="Calibri 80",anchor="c",tag="boom")    
            ara.update()
            ara.bind("<Button-1>",plane)
            break
            can.delete()
        if y1-500+30>y0+45: 
            can.delete(b)
            I=can.create_text(500,300,text="MISS",font="Calibri 80",anchor="c",tag="boom")    
            ara.update()
            ara.bind("<Button-1>",plane)
            break
            can.delete()
    ara.bind("<Button-1>",G1)
    
##функция для анимации в демонстрации
def bike():
    can.delete("boom")
    ara.unbind("<Button-1>")
    t=0
    y0=525
    y1=700
    y2=560
    g=9.8
    S=1000
    while 1==1:
        V0=70
        V2=-28
        t=t+0.025
        x1=V0*t
        x2=S+V2*t
        x3=S+V2*t+2
        x4=S+V2*t+27
        x5=V0*t+60
        y1=y0+g*(t**2)/2
        a=can.create_rectangle(x1,10,x1+60,60,fill="red")
        f=can.create_line(x5,10,x5+60,35,fill="red",width=4)
        h=can.create_line(x5,60,x5+60,35,fill="red",width=4)
        b=can.create_oval(x1,y1-500,x1+30,y1-470,fill="black")
        c=can.create_rectangle(x2,y0,x2+45,y0+45,fill="green")
        d=can.create_oval(x3,y2,x3+17,y2+17,fill="brown")
        e=can.create_oval(x4,y2,x4+17,y2+17,fill="brown")
        ara.update()
        time.sleep(0.01)
        can.delete(a)
        can.delete(b)
        can.delete(c)
        can.delete(d)
        can.delete(e)
        can.delete(f)
        can.delete(h)
        if int(x1)== int (x2):
            can.delete(b)
            e=can.create_oval(830,600,630,400,fill=random.choice(colors),outline="red",tag="boom")
            I=can.create_text(712,300,text="HIT",font="Calibri 80",anchor="c",tag="boom")    
            ara.update()
            ara.bind("<Button-1>",plane)
            break
    ara.bind("<Button-1>",G4)

def G5(event):
    x=event.x
    y=event.y
    if x>690 and x<790 and y>0 and y<50:
        ab()
    

def G4(event):
    x=event.x
    y=event.y
    if x>300 and x<400 and y>200 and y<250:
        ab()
    elif x>624 and x<724 and y>200 and y<250:
        bike()

def G3(event):
    x=event.x
    y=event.y
    if x>690 and x<790 and y>0 and y<50:
        ab()

def G1(event):
    x=event.x
    y=event.y
    if x>300 and x<400 and y>200 and y<250:
        ab()
    elif x>624 and x<724 and y>200 and y<250:
        plane()

def G2(event):
    x=event.x
    y=event.y
    if x>690 and x<790 and y>0 and y<50:
        ab()

##функция для помощи
def pun5():
    pola.place(x=780,y=1220,anchor="w")
    polv.place(x=780,y=1140,anchor="w")
    can.delete(ALL)
    can.create_rectangle(690,0,790,50,fill="gold",outline="red")
    can.create_text(740,25,text="МЕНЮ",font="Calibri 20",anchor="c")
    can.create_text(500,100,text="Помощь",font="Calibri 30",anchor="c")
    can.create_text(500,250,text="Условие-текст задачи,физический рисунок задачи.",font="Callibri 26",anchor="c")
    can.create_text(500,300,text="Краткое условие-дано,рисунок с полем ввода.",font="Callibri 26",anchor="c")
    can.create_text(500,350,text="Решение-дано,физический рисунок и физическое решение задачи.",font="Callibri 26",anchor="c")
    can.create_text(500,400,text="Демонстрация-рисунок без поля ввода, ответ.",font="Callibri 26",anchor="c")
    can.create_text(500,500,text="Чтобы выйти из любого окна,нажмите на кнопку меню.",font="Callibri 20",anchor="c")
    can.create_text(100,530,text="Чтобы в кратком условии и демонстрации начать анимацию, нажмите на кнопку пуск.",font="Callibri 20",anchor="w")
    ara.bind("<Button-1>",G5)


##функция для демонстрации
def pun4():
    pola.place(x=780,y=1220,anchor="w")
    polv.place(x=780,y=1140,anchor="w")
    can.delete(ALL)
    can.create_rectangle(300,200,400,250,fill="green",outline="red")
    can.create_rectangle(624,200,724,250,fill="green",outline="red")
    can.create_text(350,225,text="МЕНЮ",font="Calibri 20",anchor="c")
    can.create_text(674,225,text="ПУСК",font="Calibri 20",anchor="c")
    can.create_text(500,100,text="ДЕМОНСТРАЦИЯ",font="Calibri 30",anchor="c")
    can.create_text(500,150,text="Правильный ответ:S=1000м",font="Callibri 16",anchor="c")
    can.create_rectangle(0,700,1100,565,fill="green")
    ara.bind("<Button-1>",G4)

##функция для краткого условия
def pun3():
    pola.place(x=780,y=1220,anchor="w")
    polv.place(x=780,y=1140,anchor="w")
    can.delete(ALL)
    can.create_rectangle(690,0,790,50,fill="silver",outline="red")
    can.create_text(740,25,text="МЕНЮ",font="Calibri 30",anchor="c")
    can.create_text(512,50,text="Решение",font="Calibri 30",anchor="c")
    can.create_text(280,25,text="y'",font="Calibri 30",anchor="w")
    can.create_text(390,25,text="y",font="Calibri 30",anchor="w")
    can.create_text(240,120,text="h",font="Calibri 30",anchor="w")
    can.create_text(780,280,text="x",font="Calibri 30",anchor="w")
    can.create_text(570,235,text="V",font="PilGi 20",anchor="w")
    can.create_text(580,239,text="2",font="Calibri 15",anchor="w")
    can.create_text(500,325,text="S",font="Calibri 30",anchor="w")
    can.create_text(660,115,text="g",font="Kokonor 25",anchor="w")
    can.create_text(335,115,text="V",font="PilGi 20",anchor="w")
    can.create_text(345,119,text="1",font="Calibri 15",anchor="w")
##    can.create_line(520,310,495,310,arrow=FIRST,width=3)
    can.create_line(680,100,659,100,arrow=FIRST,width=3)
    can.create_line(650,140,650,105,arrow=FIRST,width=3)
    can.create_line(270,10,270,270,arrow=FIRST,width=4)
    can.create_line(380,10,380,310,arrow=FIRST,width=4)
    can.create_line(800,270,270,270,arrow=FIRST,width=4)
    can.create_line(560,251,600,251,arrow=FIRST,width=4)
    can.create_line(590,221,563,221,arrow=FIRST,width=4)
    can.create_line(370,130,326,130,arrow=FIRST,width=4)
    can.create_line(350,100,330,100,arrow=FIRST,width=4)
    can.create_line(650,300,380,300,width=4)
    can.create_line(650,310,650,270,width=4)
    can.create_rectangle(272,115,327,150,fill="red")
    can.create_rectangle(385,115,440,150,fill="orangered")
    can.create_rectangle(540,235,490,270,fill="green")
    can.create_rectangle(640,235,600,270,fill="forestgreen")
    can.create_text(10,90,text="Дано:",font="Callibri 30",anchor="w")
    can.create_text(10,120,text="h",font="Callibri 23",anchor="w")
    can.create_text(30,118,text="=250м",font="Callibri 23",anchor="w")
    can.create_text(10,140,text="V",font="PilGi 23",anchor="w")
    can.create_text(25,143,text="1",font="Callibri 16",anchor="w")
    can.create_text(35,141,text="=120 м/с",font="Callibri 23",anchor="w")
    can.create_text(10,160,text="V",font="PilGi 23",anchor="w")
    can.create_text(25,166,text="2",font="Callibri 16",anchor="w")
    can.create_text(35,163,text="=20 м/с",font="Callibri 23",anchor="w")
    can.create_text(10,200,text="S-?",font="Callibri 23",anchor="w")
    can.create_text(300,380,text="h =",font="Callibri 30",anchor="c")
    can.create_text(348,360,text="g",font="Kokonor 26",anchor="c")
    can.create_text(360,360,text="t",font="Callibri 30",anchor="c")
    can.create_text(370,350,text="2",font="Callibri 25",anchor="c")
    can.create_text(350,400,text="2",font="Callibri 30",anchor="c")
    can.create_text(300,460,text="t =",font="Callibri 30",anchor="c")
    can.create_text(405,455,text="2h",font="Callibri 30",anchor="c")
    can.create_text(408,485,text="g",font="Kokonor 30",anchor="c")
    can.create_text(405,575,text="2h",font="Callibri 30",anchor="c")
    can.create_text(405,605,text="g",font="Kokonor 30",anchor="c")
    can.create_text(355,520,text="S=(   +   )t",font="Callibri 30",anchor="c")
    can.create_text(343,522,text="V",font="PilGi 30",anchor="c")
    can.create_text(385,522,text="V",font="PilGi 30",anchor="c")
    can.create_text(355,524,text="1",font="Callibri 16",anchor="c")
    can.create_text(248,594,text="1",font="Callibri 16",anchor="c")
    can.create_text(245,590,text="S=(   +   )",font="Callibri 30",anchor="c")
    can.create_text(622,390,text="S=(",font="Callibri 30",anchor="c")
    can.create_text(675,390,text="120+",font="Callibri 25",anchor="c")
    can.create_text(722,390,text="20",font="Callibri 25",anchor="c")
    can.create_text(745,390,text=")",font="Callibri 30",anchor="c")
    can.create_text(875,369,text="2   250",font="Callibri 30",anchor="c")
    can.create_oval(851,363,861,373,fill="black")
    can.create_text(870,410,text="9,8",font="Callibri 30",anchor="c")
    can.create_text(940,390,text="=",font="Callibri 32",anchor="c")
    can.create_text(615,450,text="=",font="Callibri 35",anchor="c")
    can.create_text(625,450,text="1000м",font="Callibri 28",anchor="w")
    can.create_text(290,594,text="2",font="Callibri 16",anchor="c")
    can.create_text(237,594,text="V",font="PilGi 30",anchor="c")
    can.create_text(278,594,text="V",font="PilGi 30",anchor="c")
    can.create_text(398,524,text="2",font="Callibri 16",anchor="c")
    can.create_text(260,380,text="1)",font="Callibri 33",anchor="c")
    can.create_text(260,460,text="2)",font="Callibri 33",anchor="c")
    can.create_text(260,520,text="3)",font="Callibri 33",anchor="c")
    can.create_text(150,590,text="4)",font="Callibri 33",anchor="c")
    can.create_text(572,390,text="5)",font="Callibri 33",anchor="c")
    can.create_text(550,520,text="Ответ:S=1000м.",font="Callibri 38",anchor="w")
    can.create_line(390,380,320,380,width=4)
    can.create_line(320,460,340,460,width=4)
    can.create_line(340,460,340,490,width=4)
    can.create_line(390,430,340,490,width=4)
    can.create_line(390,430,450,430,width=4)
    can.create_line(450,430,450,460,width=4)
    can.create_line(370,470,450,470,width=4)
    can.create_line(320,580,340,580,width=4)
    can.create_line(340,580,340,610,width=4)
    can.create_line(390,550,340,610,width=4)
    can.create_line(390,550,450,550,width=4)
    can.create_line(450,550,450,580,width=4)
    can.create_line(370,590,450,590,width=4)
    can.create_line(150,75,150,280,width=5)
    can.create_line(0,180,150,180,width=5)
    can.create_line(820,390,910,390,width=4)
    can.create_line(830,340,790,413,width=4)
    can.create_line(830,340,925,340,width=4)
    can.create_line(925,340,925,375,width=4)
    can.create_line(750,390,787,390,width=4)
    can.create_line(787,390,787,415,width=4)
    can.create_arc(240,120,525,425,width=2)
    ara.bind("<Button-1>",G3)


##функция для мат.решения
def pun2():
    polv.place(x=780,y=140,anchor="w")
    can.delete(ALL)
    can.create_text(10,90,text="Дано:",font="Callibri 30",anchor="w")
    can.create_text(10,120,text="h",font="Callibri 23",anchor="w")
    can.create_text(30,118,text="=250м",font="Callibri 23",anchor="w")
    can.create_text(10,140,text="V",font="PilGi 23",anchor="w")
    can.create_text(35,141,text="=120 м/с",font="Callibri 23",anchor="w")
    can.create_text(10,160,text="V",font="PilGi 23",anchor="w")
    can.create_text(35,163,text="=20 м/с",font="Callibri 23",anchor="w")
    can.create_text(10,200,text="S-?",font="Callibri 23",anchor="w")
    can.create_text(25,143,text="1",font="Callibri 16",anchor="w")
    can.create_text(25,166,text="2",font="Callibri 16",anchor="w")
    can.create_text(780,110,text="Введите расстояние(м)",font="Callibri 20",anchor="w")
    can.create_line(150,95,150,280,width=5)
    can.create_line(0,180,150,180,width=5)
    z=can.create_text(512,100,text="Краткое условие",font="Calibri 30",anchor="c")
    can.create_rectangle(300,200,400,250,fill="pink",outline="red")
    can.create_rectangle(624,200,724,250,fill="pink",outline="red",)
    can.create_text(350,225,text="МЕНЮ",font="Calibri 20",anchor="c")
    can.create_text(674,225,text="ПУСК",font="Calibri 20",anchor="c")
    can.create_rectangle(0,700,1100,565,fill="green")
    ara.bind("<Button-1>",G1)

##функция для условия
def pun1():
    pola.place(x=780,y=1220,anchor="w")
    polv.place(x=780,y=1140,anchor="w")
    can.delete(ALL)
    can.create_text(45,545,text="На высоте 250м летит самолет со скоростью  120м/с.",font="Calibri 20",anchor="w")
    can.create_text(45,575,text="Он сбрасывает бомбу на машину, которая едет ему на встречу со скоростью 20м/с.",font="Calibri 20",anchor="w")
    can.create_text(45,605,text="На каком расстоянии от машины самолет должен сбросить бомбу?",font="Calibri 20",anchor="w")
    can.create_text(80,25,text="y'",font="Calibri 30",anchor="w")
    can.create_text(190,25,text="y",font="Calibri 30",anchor="w")
    can.create_text(40,125,text="h",font="Calibri 30",anchor="w")
    can.create_text(580,480,text="x",font="Calibri 30",anchor="w")
    can.create_text(470,435,text="V",font="PilGi 20",anchor="w")
    can.create_text(479,439,text="2",font="Calibri 17",anchor="w")
    can.create_text(300,522,text="S",font="Calibri 30",anchor="w")
    can.create_text(140,115,text="V",font="PilGi 20",anchor="w")
    can.create_text(150,118,text="1",font="Calibri 17",anchor="w")
    can.create_text(400,218,text="g",font="Kokonor 30",anchor="w")
    can.create_line(160,130,126,130,arrow=FIRST,width=4)
    can.create_line(160,102,130,102,arrow=FIRST,width=4)
    can.create_line(425,203,400,203,arrow=FIRST,width=4)
    can.create_line(390,243,390,203,arrow=FIRST,width=4)
    can.create_line(70,10,70,470,arrow=FIRST,width=4)
    can.create_line(180,10,180,510,arrow=FIRST,width=4)
    can.create_line(600,470,70,470,arrow=FIRST,width=4)
    can.create_line(465,450,490,450,arrow=FIRST,width=4)
    can.create_line(490,420,465,420,arrow=FIRST,width=4)
##    can.create_line(315,507,295,507,arrow=FIRST,width=4)
    can.create_line(450,500,180,500,width=4)
    can.create_line(450,510,450,470,width=4)
    can.create_rectangle(72,115,127,150,fill="red")
    can.create_rectangle(185,115,240,150,fill="orangered")
    can.create_rectangle(450,435,410,470,fill="green")
    can.create_rectangle(530,435,490,470,fill="forestgreen")
    can.create_text(512,100,text="УСЛОВИЕ",font="Calibri 30",anchor="c")
    can.create_rectangle(690,0,790,50,fill="darkviolet",outline="red")
    can.create_text(740,25,text="МЕНЮ",font="Calibri 20",anchor="c")
    can.create_arc(-63,120,425,825,width=3)
    ara.bind("<Button-1>",G2)
    
def P1(event):
    x=event.x
    y=event.y
    if x>455 and x<569 and y>150 and y<200:
        pun1()
    elif x>455 and x<569 and y>220 and y<270:
        pun3()
    elif x>455 and x<569 and y>290 and y<340:
        pun2()
    elif x>455 and x<569 and y>360 and y<410:
        pun4()
    elif x>455 and x<569 and y>430 and y<480:
        pun5()

def menue(event):
    ab()
    

##функция меню
def ab():
    pola.place(x=780,y=1220,anchor="w")
    polv.place(x=780,y=1140,anchor="w")
    can.delete(ALL)
    can.create_text(512,100,text="Меню",font="Calibri 50",anchor="c")
    can.create_rectangle(455,150,569,200,fill="red",outline="black")
    can.create_text(512,175,text="Условие",font="Calibri 27",anchor="c")
    can.create_rectangle(455,220,569,270,fill="red",outline="black")
    can.create_text(512,243,text="Решение",font="Calibri 27",anchor="c")
    can.create_rectangle(455,290,569,340,fill="red",outline="black")
    can.create_text(512,302,text="Краткое",font="Calibri 25",anchor="c")
    can.create_text(512,328,text="Условие",font="Calibri 25",anchor="c")
    can.create_rectangle(455,360,569,410,fill="red",outline="black")
    can.create_text(512,385,text="Демонстрация",font="Calibri 18",anchor="c")
    can.create_rectangle(455,430,569,480,fill="red",outline="black")
    can.create_text(512,455,text="ПОМОЩЬ",font="Calibri 22",anchor="c")
    can.create_text(525,530,text="Чтобы перейти в любое окно нажмите на него мышкой ",font="Calibri 22",anchor="c")
    ara.bind("<Button-1>",P1)

##функция заставки
def cd():
    can.create_text(512,25,text="Заставка",font="Calibri 35",anchor="c")
    can.create_text(512,200,text="Мелконян Маркос 8Г",font="Calibri 35",anchor="c")
    can.create_text(250,250,text="Бомбометание с горизонтально летящего с ",font="Calibri 25",anchor="w")
    can.create_text(250,280,text="постоянной скоростью самолета по мишени,",font="Calibri 25",anchor="w")
    can.create_text(250,310,text="движущейся напротив него.",font="Calibri 25",anchor="w")
    can.create_text(500,340,text="2019 год",font="Calibri 25",anchor="c")
##    can.create_rectangle(350,400,700,500,fill="white",outline="black")
    can.create_line(100,60,100,590,width=10,fill="red")
    can.create_line(120,80,120,570,width=10,fill="blue")
    can.create_line(140,100,140,550,width=10,fill="orange")
    can.create_line(100,60,900,60,width=10,fill="red")
    can.create_line(120,80,880,80,width=10,fill="blue")
    can.create_line(140,100,860,100,width=10,fill="orange")
    can.create_line(900,60,900,590,width=10,fill="red")
    can.create_line(880,80,880,570,width=10,fill="blue")
    can.create_line(860,100,860,550,width=10,fill="orange")
    can.create_line(140,550,860,550,width=10,fill="orange")
    can.create_line(120,570,880,570,width=10,fill="blue")
    can.create_line(100,590,900,590,width=10,fill="red")
    can.create_text(525,530,text="Чтобы перейти в меню, нажмите на пробел",font="Calibri 22",anchor="c")
    ara.bind("<space>",menue)
    
    

ara.bind("<Button-1>",cd)
    

cd()

ara.mainloop()
