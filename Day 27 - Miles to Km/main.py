from tkinter import *


def convert():
    miles_value = float(entry.get()) * 1.609344
    label2.config(text=miles_value)

window = Tk()
window.title("Mile to Km Convert")
window.minsize(height=150, width=300)
window.maxsize(height=150, width=300)
# window.minsize(height=200, width=200)
window.config(padx=25, pady=25)

label = Label(text="Is equal to", font=("Arial", 12))
label.grid(row=1, column=0)
label2 = Label(text="0")
label2.grid(row=1, column=5)
miles_text = Label(text="Miles")
miles_text.grid(row=0,column=6)
km = Label(text="Km")
km.grid(row=1, column = 6)


button = Button(text="Calculate", command=convert)
button.grid(row=2, column=5)

entry = Entry(width=15)
entry.grid(row=0, column=5)
# entry.focus()

mainloop()