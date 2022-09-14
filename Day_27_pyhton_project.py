from tkinter import *

window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="Miles", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=2)

my_label2 = Label(text="km", font=("Arial", 24, "bold"))
my_label2.grid(row=1, column=2)

my_label3 = Label(text="Is equal to", font=("Arial", 24, "bold"))
my_label3.grid(row=1, column=0)

my_label4 = Label(text="0", font=("Arial", 24, "bold"))
my_label4.grid(row=1, column=1)



# Button

def button_click():
    print("Button clicked")
    miles = int(input.get()) * 1.609
    my_label4.config(text= miles)


buttom = Button(text="Click me", command=button_click)
buttom.grid(column=1, row=2)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
