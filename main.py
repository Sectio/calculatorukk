from tkinter import *
from tkinter.messagebox import *
import math as m
import threading

font = ('Proxima Nova', 20, 'bold')

def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)

def all_clear():
    textField.delete(0, END)


def click_btn_function(event):
    global p
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)
    t = threading.Thread(args=(text,))
    t.start()

    if text == 'x':
        textField.insert(END, "*")
        return

    if text == '=':
        try:
            ex = textField.get()
            anser = eval(ex)
            textField.delete(0, END)
            textField.insert(0, anser)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return

    textField.insert(END, text)

window = Tk()
window.configure(background='#141414')
window.title('KALKULATOR')
window.geometry('500x450')


textField = Entry(window, font = ('Proxima Nova', 30, 'bold'), bg='#141414', fg='white', justify=RIGHT, bd='0')
textField.pack(side=TOP, pady=50, fill=X, padx=50)

buttonFrame = Frame(window)
buttonFrame.pack(side=TOP, padx=10)

temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', bg="#242323", activebackground='#242323',
                     activeforeground='white', fg='white')
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', bg="#242323", activebackground='grey',
                 activeforeground='white', fg='white')
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', bg="#242323", activebackground='#242323',
                activeforeground='white', fg='white')
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text='=', font=font, width=11, relief='ridge', bg="green", activebackground='green',
                  activeforeground='white', fg='white')
equalBtn.grid(row=4, column=2, columnspan=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', bg="#242323", activebackground='#242323',
                 activeforeground='green', fg='green',)
plusBtn.grid(row=3, column=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', bg="#242323", activebackground='#242323',
                  activeforeground='green', fg='green')
minusBtn.grid(row=2, column=3)

multBtn = Button(buttonFrame, text='x', font=font, width=5, relief='ridge', bg="#242323", activebackground='#242323',
                 activeforeground='green', fg='green')
multBtn.grid(row=1, column=3)

divideBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', bg="#242323", activebackground='#242323',
                   activeforeground='green', fg='green')
divideBtn.grid(row=0, column=3)

clearBtn = Button(buttonFrame, text='←', font=font, width=11, relief='ridge', bg="#242323", activebackground='#242323',
                  activeforeground='green', fg='green', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text='C', font=font, width=5, relief='ridge', bg="#242323", activebackground='#242323',
                     activeforeground='Red', fg='red', command=all_clear)
allClearBtn.grid(row=3, column=2)

plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)


def enterClick(event):
    print('hi')
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)

textField.bind('<Return>', enterClick)
fontMenu = ('', 15)

window.mainloop()
