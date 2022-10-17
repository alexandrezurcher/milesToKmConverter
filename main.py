from tkinter import *

def button_clicked():
    miles = float(input.get())
    label_3["text"] = round(miles * 1.609)

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=250, height=200)
window.config(padx=20, pady=20)

#Entry
input = Entry(width=10)
#input.get()
input.grid(column=3, row=2)

#Labels
label_1 = Label(text="Miles", font=("Arial", 16, "bold"))
label_1.grid(column=4, row=2)

label_2 = Label(text="is equal to", font=("Arial", 16, "bold"))
label_2.grid(column=2, row=3)

label_3 = Label(text="0", font=("Arial", 16, "bold"))
label_3.grid(column=3, row=3)

label_4 = Label(text="Km", font=("Arial", 16, "bold"))
label_4.grid(column=4, row=3)

button = Button(text="Calculate", command=button_clicked)

button.grid(column=3, row=4)

window.mainloop()
