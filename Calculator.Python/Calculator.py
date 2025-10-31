import tkinter as tk

bg_color = "#535353"
btn_color = "#ffffff"
btn_text = "#000000"
entry_bg = "#ffffff"
entry_fg = "#000000"
font_main = ("Segoe UI", 18)
font_display = ("Segoe UI", 50)
win = tk.Tk()
win.title("Calculator | DevKarimi")
win.geometry("650x600")
win.configure(bg=bg_color)

expr = ""

def press(n):
    global expr
    expr += str(n)
    eq.set(expr)

def clear():
    global expr
    expr = ""
    eq.set("Clear")

def equal():
    global expr
    try:
        res = str(eval(expr))
        eq.set(res)
        expr = res
    except:
        eq.set("Error")
        expr = ""

eq = tk.StringVar()
entry = tk.Entry(win, textvariable=eq, font=font_display, bd=10, insertwidth=2, width=14, borderwidth=4,
                 justify="right", bg=entry_bg, fg=entry_fg)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

btns = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]


for (txt, r, c) in btns:
    if txt == '=':
        cmd = equal
    elif txt == 'C':
        cmd = clear
    else:
        cmd = lambda x=txt: press(x)
    tk.Button(win, text=txt, padx=20, pady=20, font=font_main, bg=btn_color, fg=btn_text,
              command=cmd).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

for i in range(6):
    win.grid_rowconfigure(i, weight=1)
for j in range(4):
    win.grid_columnconfigure(j, weight=1)
win.mainloop()