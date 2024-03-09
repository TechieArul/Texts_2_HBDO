from tkinter import *
from tkinter import scrolledtext

dd_app = Tk()
screen_width = str(1250)
screen_height = str(750)
dd_app.geometry(f"{screen_width}x{screen_height}")
dd_app.resizable(False,False)
dd_app.title("ARUL  |  HBDO")

bg_global = "#585858"
dd_app.configure(bg=bg_global)

#func and variable
def text2bin(text):
    binary = ""
    for _char in text:
        _temp_text=str(bin(ord(_char)))
        binary+=_temp_text[0]+_temp_text[2:]+"  "
    return binary

def text2hex(text):
    hexa = ""
    for _char in text:
        hexa+=hex(ord(_char))[2:]+"  "
    return hexa

def text2oct(text):
    octal = ""
    for _char in text:
        octal+=oct(ord(_char))[2:]+"  "
    return octal

def text2dec(text):
    decimal = ""
    for _char in text:
        decimal+=str(ord(_char))+"  "
    return decimal

def remove_space(text):
    text=text.split("\n")
    print(text)
    text.pop(-1)
    print(text)
    _temp_text = ""
    for t in text:
        _temp_text+=t
    return _temp_text

def clear_text_func():
    text_input.delete('1.0',END)

    binary.configure(state="normal")
    binary.delete('1.0',END)
    binary.configure(state="disabled")

    hexa.configure(state="normal")
    hexa.delete('1.0',END)
    hexa.configure(state="disabled")
    
    octal.configure(state="normal")
    octal.delete('1.0',END)
    octal.configure(state="disabled")
    
    decimal.configure(state="normal")
    decimal.delete('1.0',END)
    decimal.configure(state="disabled")

def generate_hbdo():
    raw_text = text_input.get("1.0",END)
    if raw_text!="\n":
        text = remove_space(raw_text)

        #update bin
        binary.configure(state="normal")
        binary.delete('1.0',END)
        binary.insert(INSERT,text2bin(text))
        binary.configure(state="disabled")
        #update hex
        hexa.configure(state="normal")
        hexa.delete('1.0',END)
        hexa.insert(INSERT,text2hex(text))
        hexa.configure(state="disabled")
        #update oct
        octal.configure(state="normal")
        octal.delete('1.0',END)
        octal.insert(INSERT,text2oct(text))
        octal.configure(state="disabled")
        #update dec
        decimal.configure(state="normal")
        decimal.delete('1.0',END)
        decimal.insert(INSERT,text2dec(text))
        decimal.configure(state="disabled")

text_input_label = Label(dd_app,text="Enter a Text    ",font=("impact",15),bg=bg_global,fg="orange")
text_input_label.place(x=250,y=50)
text_input = scrolledtext.ScrolledText(dd_app,width=40,height=3,font=(None,18),bg=bg_global,fg="orange",)
text_input.place(x=250,y=90)

binary_label = Label(dd_app,text="Binary    ",font=("impact",15),bg=bg_global,fg="#ffe435")
binary_label.place(x=250,y=200)
binary = scrolledtext.ScrolledText(dd_app,width=47,height=3,font=(None,15),bg=bg_global,fg="white",)
binary.place(x=250,y=240)

hexa_label = Label(dd_app,text="Hexadecimal    ",font=("impact",15),bg=bg_global,fg="#ffe435")
hexa_label.place(x=250,y=350)
hexa = scrolledtext.ScrolledText(dd_app,width=47,height=2,font=(None,15),bg=bg_global,fg="white",)
hexa.place(x=250,y=390)

octal_label = Label(dd_app,text="Octal    ",font=("impact",15),bg=bg_global,fg="#ffe435")
octal_label.place(x=250,y=500)
octal = scrolledtext.ScrolledText(dd_app,width=47,height=2,font=(None,15),bg=bg_global,fg="white",)
octal.place(x=250,y=540)

decimal_label = Label(dd_app,text="Decimal    ",font=("impact",15),bg=bg_global,fg="#ffe435")
decimal_label.place(x=250,y=640)
decimal = scrolledtext.ScrolledText(dd_app,width=47,height=2,font=(None,15),bg=bg_global,fg="white",state="disabled")
decimal.place(x=250,y=680)
# decimal.configure(state="normal")

generate_button = Button(dd_app,text="GET    HBDO",width=13,font=("impact",15),bg="orange",fg="black",activeforeground="orange",activebackground="black",command=generate_hbdo)
generate_button.place(x=850,y=90)

clear_text = Button(dd_app,text="C l e a r",width=10,font=("impact",15),bg="orange",fg="black",activeforeground="orange",activebackground="black",command=clear_text_func)
clear_text.place(x=1030,y=90)




dd_app.mainloop()
