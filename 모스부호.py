from tkinter import *
 
root = Tk()
root.title('모스부호')
 
text = Entry(root, width=35)
text.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipady= 5)
brain = Entry(root, width=35)
brain.grid(row=3, column=0, columnspan=3, padx=10, pady=10, ipady= 5)
def button_click(sign):
    current = text.get()
    text.delete(0, END)
    text.insert(0,str(current) + str(sign))
                
def button_trans():
    inputsign = text.get()
    if inputsign == '.ㅡ':
        text.delete(0, END)
        text.insert(0, str('A'))
    if inputsign == 'ㅡ...':
        text.delete(0, END)
        text.insert(0, str('B'))
    if inputsign == 'ㅡ.ㅡ.':
        text.delete(0, END)
        text.insert(0, str('C'))
    if inputsign == 'ㅡ..':
        text.delete(0, END)
        text.insert(0, str('D'))
    if inputsign == '.':
        text.delete(0, END)
        text.insert(0, str('E'))
    if inputsign == '..ㅡ.':
        text.delete(0, END)
        text.insert(0, str('F'))
    if inputsign == 'ㅡㅡ.':
        text.delete(0, END)
        text.insert(0, str('G'))
    if inputsign == '....':
        text.delete(0, END)
        text.insert(0, str('H'))
    if inputsign == '..':
        text.delete(0, END)
        text.insert(0, str('I'))
    if inputsign == '.ㅡㅡㅡ':
        text.delete(0, END)
        text.insert(0, str('J'))
    if inputsign == 'ㅡ.ㅡ':
        text.delete(0, END)
        text.insert(0, str('K'))
    if inputsign == '.ㅡ..':
        text.delete(0, END)
        text.insert(0, str('L'))
    if inputsign == 'ㅡㅡ':
        text.delete(0, END)
        text.insert(0, str('M'))
    if inputsign == 'ㅡ.':
        text.delete(0, END)
        text.insert(0, str('N'))
    if inputsign == 'ㅡㅡㅡ':
        text.delete(0, END)
        text.insert(0, str('O'))
    if inputsign == '.ㅡㅡ.':
        text.delete(0, END)
        text.insert(0, str('P'))
    if inputsign == '.ㅡㅡ.ㅡ':
        text.delete(0, END)
        text.insert(0, str('Q'))
    if inputsign == '.ㅡ.':
        text.delete(0, END)
        text.insert(0, str('R'))
    if inputsign == '...':
        text.delete(0, END)
        text.insert(0, str('S'))
    if inputsign == 'ㅡ':
        text.delete(0, END)
        text.insert(0, str('T'))
    if inputsign == '..ㅡ':
        text.delete(0, END)
        text.insert(0, str('U'))
    if inputsign == '...ㅡ':
        text.delete(0, END)
        text.insert(0, str('V'))
    if inputsign == '.ㅡㅡ':
        text.delete(0, END)
        text.insert(0, str('W'))
    if inputsign == 'ㅡ..ㅡ':
        text.delete(0, END)
        text.insert(0, str('X'))
    if inputsign == 'ㅡ.ㅡㅡ':
        text.delete(0, END)
        text.insert(0, str('Y'))
    if inputsign == 'ㅡㅡ..':
        text.delete(0, END)
        text.insert(0, str('Z'))
def button_clear():
    text.delete(0, END)
def button_memorize():
    memory1 = text.get()
    memory2 = brain.get()
    brain.delete(0, END)
    brain.insert(0, str(memory2) + str(memory1))
    
    
button_transform = Button(root, text='변환', padx=30, pady=20, command=button_trans)
button_1 = Button(root, text='.', padx=40, pady=20, command=lambda : button_click('.'))
button_2 = Button(root, text='ㅡ', padx=40, pady=20, command=lambda : button_click('ㅡ'))
button_clean = Button(root, text='지우기', padx=30, pady=20, command=button_clear)
button_mem = Button(root, text='저장', padx=30, pady=20, command=button_memorize)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_transform.grid(row=5, column=0)
button_clean.grid(row=7, column=1)
button_mem.grid(row=7, column=0)

root.mainloop()