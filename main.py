import tkinter.messagebox as msgbox
import pandas as pd
from math import *
from tkinter import *

#----------메뉴-----------

def credit():
    creditwin = Toplevel(root)
    creditwin.geometry('320x200+100+100')
    creditname = Label(creditwin, text = '천능 계산기', font = 30).pack()
    creditmans = Message(creditwin, width = 300, text = '만든이 : 신동흠, 이윤민, 노광민, 김민기\n태성고등학교 HACKATON\nPython 3 사용').pack()
    

def quitConfirm():
    response = msgbox.askyesno('종료', '종료하시겠습니까?')
    if response == 1:
        close()
    
def close():
    root.quit()
    root.destroy()

#----------연산-----------

def btn_num(number):
    current = result.get()
    if (current == '0') and (number == 0):
        pass
    else:
        result.delete(0, END)
        result.insert(0, str(current) + str(number))

def btn_dot():
    current = result.get()
    if current.find('.') != -1:
        pass
    else:
        result.delete(0, END)
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
    try:
        if math == '더하기':
            result.insert(0, round(f_num + float(second_number), 7))
        if math == '빼기':
            result.insert(0, round(f_num - float(second_number), 7))
        if math == '곱하기':
            result.insert(0, round(f_num * float(second_number), 7))
        if math == '나누기':
            if second_number == '0':
                result.insert(0, 'ERROR')
            else:
                result.insert(0, round(f_num / float(second_number), 7))
        if math == '제곱':
            result.insert(0, round(f_num ** float(second_number), 7))
    except:
        pass
 
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
    if raddeg.get() == 0:
        result.insert(0, round(sin(radians(float(inputnumber))), 7))
    elif raddeg.get() == 1:
        result.insert(0, round(sin(float(inputnumber)), 7))

def btn_cos():
    inputnumber = result.get()
    result.delete(0, END)
    if raddeg.get() == 0:
        result.insert(0, round(cos(radians(float(inputnumber))), 7))
    elif raddeg.get() == 1:
        result.insert(0, round(cos(float(inputnumber)), 7))

def btn_tan():
    inputnumber = result.get()
    result.delete(0, END)
    if raddeg.get() == 0:
        if (int(inputnumber) % 90 == 0) and ((int(inputnumber) // 90) % 2 == 1):
            result.insert(0, 'ERROR')
        else:
            result.insert(0, round(tan(radians(float(inputnumber))), 7))

    elif raddeg.get() == 1:
        if (round(float(inputnumber) % 1.5707963) == 0) and (round(float(inputnumber) // 1.5707963 % 2) == 1):
            result.insert(0, 'ERROR')
        else:
            result.insert(0, round(tan(float(inputnumber)), 7))

def btn_pi():
    result.delete(0, END)
    result.insert(0, round(pi, 7))

def btn_sqrt():
    inputnumber = result.get()
    result.delete(0, END)
    result.insert(0, round(sqrt(float(inputnumber)), 7))

def btn_power():
    first_number = result.get()
    global f_num
    global math
    math = '제곱'
    f_num = float(first_number)
    result.delete(0, END)

def btn_log():
    inputnumber = result.get()
    result.delete(0, END)
    if float(inputnumber) <= 0:
        result.insert(0, 'ERROR')
    else:
        result.insert(0, round(log10(float(inputnumber)), 7))
#----------GUI-----------

pd.options.display.float_format = '{:.7f}'.format
root = Tk() #GUI 생성
root.title('Calculator') #GUI 제목
root.geometry('600x550')
root.resizable(False, False) #GUI 크기 조정 불가

menubar = Menu(root)
menu_1 = Menu(menubar, tearoff = 0)
menu_1.add_command(label = '만든이', command = credit)
menu_1.add_separator()
menu_1.add_command(label = '닫기', command = quitConfirm)
menubar.add_cascade(label = '메뉴', menu = menu_1)

menu_2 = Menu(menubar, )
root.config(menu = menubar)

label = Label(root, text = '만능은 아니구 천능 계산기', font=30, pady = 10)
label.pack()

result = Entry(root, text = '0', font = 30, justify = 'right', background='white')
result.place(x = 50, y = 60, width = 500, height = 30)

raddeg = IntVar()
rad2deg = Radiobutton(root, text = 'Degree', value = 0, variable=raddeg).place(x = 50, y = 100)
deg2rad = Radiobutton(root, text = 'Radian', value = 1, variable=raddeg).place(x = 150, y = 100)


b1 = Button(root, text = '1', font = 30, cursor = 'hand2', relief = 'groove', command=lambda : btn_num(1)).place(x = 200, y = 150, width = 100, height = 100)
b2 = Button(root, text = '2', font = 30, cursor = 'hand2', relief = 'groove', command=lambda : btn_num(2)).place(x = 300, y = 150, width = 100, height = 100)
b3 = Button(root, text = '3', font = 30, cursor = 'hand2', relief = 'groove', command=lambda : btn_num(3)).place(x = 400, y = 150, width = 100, height = 100)
b4 = Button(root, text = '4', font = 30, cursor = 'hand2', relief = 'groove', command=lambda : btn_num(4)).place(x = 200, y = 250, width = 100, height = 100)
b5 = Button(root, text = '5', font = 30, cursor = 'hand2', relief = 'groove', command=lambda : btn_num(5)).place(x = 300, y = 250, width = 100, height = 100)
b6 = Button(root, text = '6', font = 30, cursor = 'hand2', relief = 'groove', command=lambda : btn_num(6)).place(x = 400, y = 250, width = 100, height = 100)
b7 = Button(root, text = '7', font = 30, cursor = 'hand2', relief = 'groove', command=lambda : btn_num(7)).place(x = 200, y = 350, width = 100, height = 100)
b8 = Button(root, text = '8', font = 30, cursor = 'hand2', relief = 'groove', command=lambda : btn_num(8)).place(x = 300, y = 350, width = 100, height = 100)
b9 = Button(root, text = '9', font = 30, cursor = 'hand2', relief = 'groove', command=lambda : btn_num(9)).place(x = 400, y = 350, width = 100, height = 100)
b0 = Button(root, text = '0', font = 30, cursor = 'hand2', relief = 'groove', command=lambda : btn_num(0)).place(x = 200, y = 450, width = 100, height = 100)

bclear = Button(root, text = 'Clear', font = 30, background = 'orange', cursor = 'hand2', relief = 'groove', command = btn_clear).place(x = 100, y = 450, width = 100, height = 100)
bequal = Button(root, text = '=', font = 30, background = 'orange', cursor = 'hand2', relief = 'groove', command = btn_equal).place(x = 400, y = 450, width = 100, height = 100)
bsum = Button(root, text = '+', font = 30, cursor = 'hand2', relief = 'groove', command = btn_add).place(x = 500, y = 150, width = 100, height = 100)
bsub = Button(root, text = '-', font = 30, cursor = 'hand2', relief = 'groove', command = b_subtract).place(x = 500, y = 250, width = 100, height = 100)
bmult = Button(root, text = '*', font = 30, cursor = 'hand2', relief = 'groove', command = btn_multiply).place(x = 500, y = 350, width = 100, height = 100)
bdiv = Button(root, text = '/', font = 30, cursor = 'hand2', relief = 'groove', command = btn_divide).place(x = 500, y = 450, width = 100, height = 100)

bsqrt = Button(root, text = '√', font = 30, cursor = 'hand2', relief = 'groove', command = btn_sqrt).place(x = 100, y = 150, width = 100, height = 100)
bpower = Button(root, text = '^', font = 30, cursor = 'hand2', relief = 'groove', command = btn_power).place(x = 100, y = 250, width = 100, height = 100)
blog = Button(root, text = 'log', font = 30, cursor = 'hand2', relief = 'groove', command = btn_log).place(x = 100, y = 350, width = 100, height = 100)
ddot = Button(root, text = '.', font = 30, cursor = 'hand2', relief = 'groove', command = btn_dot).place(x = 300, y = 450, width = 100, height = 100)

bsin = Button(root, text = 'sin', font = 30, cursor = 'hand2', relief = 'groove', command = btn_sin).place(x = 0, y = 150, width = 100, height = 100)
bcos = Button(root, text = 'cos', font = 30, cursor = 'hand2', relief = 'groove', command = btn_cos).place(x = 0, y = 250, width = 100, height = 100)
btan = Button(root, text = 'tan', font = 30, cursor = 'hand2', relief = 'groove', command = btn_tan).place(x = 0, y = 350, width = 100, height = 100)
bpi = Button(root, text = 'π', font = 30, cursor = 'hand2', relief = 'groove', command = btn_pi).place(x = 0, y = 450, width = 100, height = 100)

#-----------실행과 종료 보고-------------

root.mainloop()

print('Programm Terminated')