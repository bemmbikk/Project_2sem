from tkinter import*
from tkinter.ttk import Combobox
import tkinter.ttk as ttk
from tkcalendar import DateEntry


root = Tk()
root.title("Задание 1")
root.geometry('700x550')


tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Скидка')
tab_control.add(tab2, text='Условия')
tab_control.add(tab3, text='Ограничения')
tab_control.add(tab4, text='Купоны')
tab_control.add(tab5, text='Дополнительно')


lab0 = Label(tab1, text='Параметры скидки', font=("Arial", 15, 'bold'))
lab1 = Label(tab1, text="Активность: ", font=("Arial", 10))
lab2 = Label(tab1, text="Название: ", font=("Arial", 10, 'bold'))
lab3 = Label(tab1, text="Сайт: ", font=("Arial", 10, 'bold'))
lab4 = Label(tab1, text="Период активности: ", font=("Arial", 10))
lab5 = Label(tab1, text="Тип скидки: ", font=("Arial", 10, 'bold'))
lab6 = Label(tab1, text="Величина скидки: ", font=("Arial", 10, 'bold'))
lab7 = Label(tab1, text="Валюта скидки: ", font=("Arial", 10, 'bold'))
lab8 = Label(tab1, text="Максимальная валюта скидки (в валюте скидки;", font=("Arial", 10))
lab9 = Label(tab1, text="Применяется к продлению подписки: ", font=("Arial", 10))
lab10 = Label(tab1, text="Приоритет применимости: ", font=("Arial", 10))
lab11 = Label(tab1, text="Прекратить дальнейшее применение скидок: ", font=("Arial", 10))
lab12 = Label(tab1, text="Краткое описание (до 255 символов): ", font=("Arial", 10))
lab13 = Label(tab1, text="0 - скидка не ограничена): ", font=("Arial", 10))

lab0.place(x=10, y=9)  # Параметры скидки
lab1.place(x=252, y=55)  # Активность
lab2.place(x=254, y=80)  # Название
lab3.place(x=286, y=105)  # Сайт
lab4.place(x=203, y=130)  # Период активности
lab5.place(x=242, y=155)  # Тип скидки
lab6.place(x=201, y=180)  # Величина скидки
lab7.place(x=215, y=205)  # Валюта скидки
lab8.place(x=27, y=230)  # Макс. валюта..
lab13.place(x=162, y=248)
lab9.place(x=96, y=273)  # Применение..
lab10.place(x=164, y=298)  # Приоритет..
lab11.place(x=48, y=323)  # Прекратить..
lab12.place(x=95, y=348)  # Краткое описание


txt1 = Entry(tab1, width=35)
txt2 = Entry(tab1, width=45)
txt3 = Entry(tab1, width=45)
txt4 = Entry(tab1, width=45)
txt5 = Text(tab1, height=7, width=35)

txt1.place(x=330, y=82)
txt2.place(x=330, y=183)
txt3.place(x=330, y=242)
txt4.place(x=330, y=300)
txt5.place(x=330, y=352)


list1 = Combobox(tab1, height=3, width=17, font=("Arial", 10))
list1['values'] = ("(s1)Моя компания", "(s2)Моя компания")
list1.current(1)
list1.place(x=330, y=106)

list2 = Combobox(tab1, height=3, width=13, font=("Arial", 10), background='azure')
list2['values'] = ("Интервал", "Без интервала")
list2.current(1)
list2.place(x=330, y=131)

list3 = Combobox(tab1, height=3, width=5, font=("Arial", 10), background='azure')
list3['values'] = ("USD", "EUR", "RUB")
list3.current(1)
list3.place(x=330, y=207)

list4 = Combobox(tab1, height=3, width=20, font=("Arial", 10), background='azure')
list4['values'] = ("В процентах", "Фиксированная сумма")
list4.current(1)
list4.place(x=330, y=155)


but1 = Button(tab1, text='Сохранить', width=10, bg='chartreuse3')
but2 = Button(tab1, text='Применить', width=10)
but3 = Button(tab1, text='Отменить', width=10)

but1.place(x=10, y=490)
but2.place(x=95, y=490)
but3.place(x=180, y=490)


ch = Checkbutton(tab1)
ch.place(x=327, y=56)

ch = Checkbutton(tab1)
ch.place(x=327, y=274)

ch = Checkbutton(tab1)
ch.place(x=327, y=324)


cul1 = DateEntry(tab1, width=12, year=2014, month=3, day=17, bd='gray57', fd='white', borderwidth=2)
cul1.place(x=450, y=131)

cul2 = DateEntry(tab1, width=12, year=2014, month=4, day=17, bd='gray57', fd='white', borderwidth=2)
cul2.place(x=550, y=131)


tab_control.pack(expand=5, fill='both')
root.mainloop()
