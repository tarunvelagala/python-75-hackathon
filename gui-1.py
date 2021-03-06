from tkinter import *
from tkinter import messagebox
import _tkinter
window = Tk()


def output():
    try:
        hex_output = str(hex(input1.get())[2:]).upper()
        bin_output = str(bin(input1.get())[2:]).upper()
        oct_output = str(oct(input1.get())[2:]).upper()
        l2_output.config(text=bin_output)
        l3_output.config(text=hex_output)
        l4_output.config(text=oct_output)
        Label(window).grid(row=4, column=1)
    except _tkinter.TclError as tkerror:
        messagebox.showerror('Input Error', 'Please input a value')
        l2_output.config(text="")
        l3_output.config(text="")
        l4_output.config(text="")


def reset():
    l1_entry.delete(0, 'end')
    l2_output.config(text="")
    l3_output.config(text="")
    l4_output.config(text="")


window.geometry("700x500")
l1_input = Label(window, text='INPUT', pady=20, font=("Roboto", 13, 'bold'))
l1_input.grid(row=0, column=0)
input1 = IntVar()
l1_entry = Entry(textvariable=input1, font=("Roboto", 13, 'bold'))
l1_entry.grid(row=0, column=1)
l2_input = Label(window, text='BINARY', pady=20, font=("Roboto", 13, 'bold'))
l2_input.grid(row=1, column=0)
l2_output = Label(window, fg="green", font=("Roboto", 13, 'bold'))
l2_output.grid(row=1, column=1)
l3_input = Label(window, text='HEXA DECIMAL',
                 pady=20, font=("Roboto", 13, 'bold'))
l3_input.grid(row=2, column=0)
l3_output = Label(window, fg="blue", font=("Roboto", 13, 'bold'))
l3_output.grid(row=2, column=1)
l4_input = Label(window, text='OCTAL', pady=20, font=("Roboto", 13, 'bold'))
l4_input.grid(row=3, column=0)
l4_output = Label(window, fg="red", font=("Roboto", 13, 'bold'))
l4_output.grid(row=3, column=1)
b1 = Button(window, text='Calculate', command=output, font=("Roboto", 10))
b1.grid(column=1, row=5)
b2 = Button(window, text='Reset', command=reset, font=("Roboto", 10))
b2.grid(column=2, row=5)
window.mainloop()
