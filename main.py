import tkinter.messagebox as msgbox
from math import *
from tkinter import *

#---------------------

def quitConfirm():
    response = msgbox.askyesno('종료', '종료하시겠습니까?')
    if response == 1:
        close()
    
def close():
    cal.quit()
    cal.destroy()

#---------------------

def btn_num(number):
    current = result.get()
    if (current == '0') and (number == 0):
        pass
    else:
        result.delete(0, END)
        result.insert(0, str(current) + str(number))

def btn_dot():
    current = result.get()
    result.delete(0,)
    result.insert(0, str(current) + '.')

def btn_clear():
    result.delete(0, END)
 
def btn_add():
    first_number = result.get()
    global math
    global f_num
    math = '더하기'
    f_num = float(first_number)
    result.delete(0, END)
 
def btn_equal():
    second_number = result.get()
    result.delete(0, END)
 
    if math == '더하기':
        result.insert(0, f_num + float(second_number))
    if math == '빼기':
        result.insert(0, f_num - float(second_number))
    if math == '곱하기':
        result.insert(0, f_num * float(second_number))
    if math == '나누기':
        result.insert(0, f_num / float(second_number))
    if math == '제곱':
        result.insert(0, f_num ** float(second_number))
 
def b_subtract():
    first_number = result.get()
    global f_num
    global math
    math = '빼기'
    f_num = float(first_number)
    result.delete(0, END)
 
def btn_multiply():
    first_number = result.get()
    global f_num
    global math
    math = '곱하기'
    f_num = float(first_number)
    result.delete(0, END)
 
def btn_divide():
    first_number = result.get()
    global f_num
    global math
    math = '나누기'
    f_num = float(first_number)
    result.delete(0, END)

def btn_sin():
    inputnumber = result.get()
    result.delete(0, END)
    result.insert(0, round(sin(radians(int(inputnumber))), 5))

def btn_cos():
    inputnumber = result.get()
    result.delete(0, END)
    result.insert(0, round(cos(radians(int(inputnumber))), 5))

def btn_tan():
    inputnumber = result.get()
    result.delete(0, END)
    if (int(inputnumber) % 90 == 0) and ((int(inputnumber) // 90) % 2 != 0):
        result.delete(0, END)
        result.insert(0, 'ERROR')
    else:
        result.insert(0, round(tan(radians(int(inputnumber))), 5))

def btn_pi():
    result.delete(0, END)
    result.insert(0, round(pi, 5))

def btn_power():
    first_number = result.get()
    global f_num
    global math
    math = '제곱'
    f_num = float(first_number)
    result.delete(0, END)
#---------------------

cal = Tk() #GUI 생성
cal.title('Calculator') #GUI 제목
cal.geometry('600x500')
cal.resizable(False, False) #GUI 크기 조정 불가

menubar = Menu(cal)
menu_1 = Menu(menubar, tearoff = 0)
menu_1.add_command(label = '천능 계산기')
menu_1.add_command(label = '물리량 계산기')
menu_1.add_separator()
menu_1.add_command(label = '닫기', command = quitConfirm)
menubar.add_cascade(label = '메뉴', menu = menu_1)

menu_2 = Menu(menubar, )
cal.config(menu = menubar)

label = Label(cal, text = '천능 계산기', font=30, pady = 10)
label.pack()

result = Entry(cal, text = '0', font = 30, justify = 'right', background='white')
result.place(x = 50, y = 60, width = 500, height = 30)

b1 = Button(cal, text = '1', font = 30, command=lambda : btn_num(1)).place(x = 200, y = 100, width = 100, height = 100)
b2 = Button(cal, text = '2', font = 30, command=lambda : btn_num(2)).place(x = 300, y = 100, width = 100, height = 100)
b3 = Button(cal, text = '3', font = 30, command=lambda : btn_num(3)).place(x = 400, y = 100, width = 100, height = 100)
b4 = Button(cal, text = '4', font = 30, command=lambda : btn_num(4)).place(x = 200, y = 200, width = 100, height = 100)
b5 = Button(cal, text = '5', font = 30, command=lambda : btn_num(5)).place(x = 300, y = 200, width = 100, height = 100)
b6 = Button(cal, text = '6', font = 30, command=lambda : btn_num(6)).place(x = 400, y = 200, width = 100, height = 100)
b7 = Button(cal, text = '7', font = 30, command=lambda : btn_num(7)).place(x = 200, y = 300, width = 100, height = 100)
b8 = Button(cal, text = '8', font = 30, command=lambda : btn_num(8)).place(x = 300, y = 300, width = 100, height = 100)
b9 = Button(cal, text = '9', font = 30, command=lambda : btn_num(9)).place(x = 400, y = 300, width = 100, height = 100)
b0 = Button(cal, text = '0', font = 30, command=lambda : btn_num(0)).place(x = 300, y = 400, width = 100, height = 100)

bclear = Button(cal, text = 'Clear', font = 30,background = 'orange', command = btn_clear).place(x = 100, y = 400, width = 100, height = 100)
bequal = Button(cal, text = '=', font = 30, background = 'orange', command = btn_equal).place(x = 400, y = 400, width = 100, height = 100)
bsum = Button(cal, text = '+', font = 30, command = btn_add).place(x = 500, y = 100, width = 100, height = 100)
bsub = Button(cal, text = '-', font = 30, command = b_subtract).place(x = 500, y = 200, width = 100, height = 100)
bmult = Button(cal, text = '*', font = 30, command = btn_multiply).place(x = 500, y = 300, width = 100, height = 100)
bdiv = Button(cal, text = '/', font = 30, command = btn_divide).place(x = 500, y = 400, width = 100, height = 100)

bsqrt = Button(cal, text = '√', font = 30).place(x = 100, y = 100, width = 100, height = 100)
bpower = Button(cal, text = '^', font = 30, command = btn_power).place(x = 100, y = 200, width = 100, height = 100)
blog = Button(cal, text = 'log', font = 30).place(x = 100, y = 300, width = 100, height = 100)
ddot = Button(cal, text = '.', font = 30, command = btn_dot).place(x = 200, y = 400, width = 100, height = 100)

bsin = Button(cal, text = 'sin', font = 30, command = btn_sin).place(x = 0, y = 100, width = 100, height = 100)
bcos = Button(cal, text = 'cos', font = 30, command = btn_cos).place(x = 0, y = 200, width = 100, height = 100)
btan = Button(cal, text = 'tan', font = 30, command = btn_tan).place(x = 0, y = 300, width = 100, height = 100)
bpi = Button(cal, text = 'π', font = 30, command = btn_pi).place(x = 0, y = 400, width = 100, height = 100)

#------------------------

cal.mainloop()

print('Programm Terminated')