from tkinter import *

# event.widget.cget('text')
# this is used to get the text of the button
# eval() this will evaluate the string as combination of operands and operators


# GUI PART
root = Tk()

root.geometry('390x750')
root.maxsize(width=390, height=750)
root.minsize(width=390, height=750)
root.wm_iconbitmap("calu_icon.ico")
root.title('CALCULATOR')
root.state('zoomed')

frame1 = Frame(root, background='black')
frame1.pack(fill=X, padx=10)

p = StringVar()
p.set('')

t1 = Entry(frame1, font='lucida 20 bold', textvariable=p)
t1.pack(fill=X, padx=8, pady=20)


# Function part
def seven():
    global p
    if p.get() == '0':
        string = str(7)
        p.set(string)
    else:
        string = f'{str(p.get())}7'
        print(string)
        p.set(string)


def eight():
    global p
    if p.get() == '0':
        string = str(8)
        p.set(string)
    else:
        string = f'{str(p.get())}8'
        # print (string)
        p.set(string)


def nine():
    global p
    if p.get() == '0':
        string = str(9)
        p.set(string)
    else:
        string = f'{str(p.get())}9'
        # print (string)
        p.set(string)


def divide():
    global p
    if p.get() == '0':
        string = str('/')
        p.set(string)

    else:
        string = f'{str(p.get())}/'
        # print (string)
        p.set(string)


def four():
    global p
    if p.get() == '0':
        string = str(4)
        p.set(string)
    else:
        string = f'{str(p.get())}4'
        # print (string)
        p.set(string)


def five():
    global p
    if p.get() == '0':
        string = str(5)
        p.set(string)
    else:
        string = f'{str(p.get())}5'
        # print (string)
        p.set(string)


def six():
    global p
    if p.get() == '0':
        string = str(6)
        p.set(string)
    else:
        string = f'{str(p.get())}6'
        # print (string)
        p.set(string)


def multiply():
    global p
    if p.get() == '0':
        string = str('*')
        p.set(string)
    else:
        string = f'{str(p.get())}*'
        # print (string)
        p.set(string)


def one():
    global p
    if p.get() == '0':
        string = str(1)
        p.set(string)
    else:
        string = f'{str(p.get())}1'
        # print (string)
        p.set(string)


def two():
    global p
    if p.get() == '0':
        string = str(2)
        p.set(string)
    else:
        string = f'{str(p.get())}2'
        # print (string)
        p.set(string)


def three():
    global p
    if p.get() == '0':
        string = str(3)
        p.set(string)
    else:
        string = f'{str(p.get())}3'
        # print (string)
        p.set(string)


def subtract():
    global p
    if p.get() == '0':
        string = str('-')
        p.set(string)
    else:
        string = f'{str(p.get())}-'
        # print (string)
        p.set(string)


def point():
    global p
    if p.get() == '0':
        return None
    else:
        string = f'{str(p.get())}.'
        # print(string)
        p.set(string)


def zero():
    global p
    if p.get() == '0':
        return None
    else:
        string = f'{str(p.get())}0'
        # print(string)
        p.set(string)


def plus():
    global p
    if p.get() == '0':
        string = str('+')
        p.set(string)
    else:
        string = f'{str(p.get())}+'
        # print(string)
        p.set(string)


memorylist = []


def equal(useless=0):
    ans = eval(p.get())
    # ans = response["choices"][0]["text"]
    print(ans)
    p.set(ans)
    lis.insert(END, ans)
    memorylist.append(ans)
    return useless


def percent():
    global p
    if p.get() == '0':
        return None
    else:
        l = len(str(p.get()))
        pstring = str(p.get())
        if pstring[len(pstring) - 3] == '+' or pstring[len(pstring) - 3] == '-':
            string = f'{pstring[len(pstring) - 1]}*{pstring}'
            pass
        else:
            string = f'{str(p.get())}/100'
            # print(string)
        p.set(string)


def ce():
    global p
    p.set('')


def back():
    r = str(p.get())
    li = list(r)
    # print(li)
    li.pop()
    # print(li)
    r = ''
    for i in li:
        r = r + i

    p.set(r)


def butt():
    global p
    # print (lis.curselection())
    turple = lis.curselection()
    # print (memorylist[turple[0]])
    string = f'{p.get()}{memorylist[turple[0]]}'
    p.set(string)


# t1.bind("<Return>", equal)

frame2 = Frame(root, bg='grey')
frame2.pack(fill=X, padx=10)

Button(frame2, text='7', font='Lucida 20 bold', padx=20, command=seven).pack(side=LEFT, padx=7, pady=3)

Button(frame2, text='8', font='Lucida 20 bold', padx=20, command=eight).pack(side=LEFT, padx=7, pady=3)

Button(frame2, text='9', font='Lucida 20 bold', padx=20, command=nine).pack(side=LEFT, padx=7, pady=3)

Button(frame2, text='/', font='Lucida 20 bold', padx=22, command=divide).pack(side=LEFT, padx=7, pady=3)

frame3 = Frame(root, bg='grey')
frame3.pack(fill=X, padx=10)

Button(frame3, text='4', font='Lucida 20 bold', padx=20, command=four).pack(side=LEFT, padx=7, pady=3)

Button(frame3, text='5', font='Lucida 20 bold', padx=20, command=five).pack(side=LEFT, padx=7, pady=3)

Button(frame3, text='6', font='Lucida 20 bold', padx=20, command=six).pack(side=LEFT, padx=7, pady=3)

Button(frame3, text='*', font='Lucida 20 bold', padx=20, command=multiply).pack(side=LEFT, padx=7, pady=3)

frame4 = Frame(root, bg='grey')
frame4.pack(fill=X, padx=10)

Button(frame4, text='1', font='Lucida 20 bold', padx=20, command=one).pack(side=LEFT, padx=7, pady=3)

Button(frame4, text='2', font='Lucida 20 bold', padx=20, command=two).pack(side=LEFT, padx=7, pady=3)

Button(frame4, text='3', font='Lucida 20 bold', padx=20, command=three).pack(side=LEFT, padx=7, pady=3)

Button(frame4, text='-', font='Lucida 20 bold', padx=21, command=subtract).pack(side=LEFT, padx=7, pady=3)

frame5 = Frame(root, bg='grey')
frame5.pack(fill=X, padx=10)

frame7 = Frame(root, bg='grey')
frame7.pack(fill=X, padx=10)

Button(frame5, text='.', font='Lucida 20 bold', padx=24, command=point).pack(side=LEFT, padx=7, pady=3)

Button(frame5, text='0', font='Lucida 20 bold', padx=20, command=zero).pack(side=LEFT, padx=7, pady=3)

Button(frame5, text='⌫', font='Lucida 20 bold', padx=10, command=back).pack(side=LEFT, padx=7, pady=3)

Button(frame5, text='+', font='Lucida 20 bold', padx=18, command=plus).pack(side=LEFT, padx=7, pady=3)

Button(frame7, text='%', font='Lucida 20 bold', padx=16, command=percent).pack(side=LEFT, padx=7, pady=3)

Button(frame7, text='CE', font='Lucida 20 bold', padx=9, command=ce).pack(side=LEFT, padx=7, pady=3)

Button(frame7, text='=', font='Lucida 20 bold', bg='green', fg='white', padx=19, command=equal).pack(side=LEFT, padx=7,
                                                                                                     pady=3)

Button(frame7, text='EXIT', font='Lucida 18 bold', pady=2, command=quit, bg='red', fg='white').pack(side=LEFT, padx=5,
                                                                                                    pady=3)

frame6 = Frame(root, bg='grey')
frame6.pack(fill=X, padx=10)

meml1 = Label(frame6, text="MEMORY", font="algerian 20 bold underline", bg='grey')
meml1.pack(anchor=W, pady=5, padx=5)

lis = Listbox(frame6, font='lucida 16 bold')
lis.pack(fill=X, padx=5, pady=5)
Button(frame6, text='add to evaluation', command=butt, bg='black', fg='white').pack(anchor=W, pady=5, padx=5)

root.mainloop()
