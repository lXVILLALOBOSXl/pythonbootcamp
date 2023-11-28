from tkinter import *


def calculate():
    km = str(float(input_miles.get()) * 1.609344)
    output_km.config(state="normal")
    output_km.insert(0, km)
    output_km.config(state="disabled")



#  Window 
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=100, height=50)
window.config(padx=10, pady=10)

# Miles Entry
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# Equal Label
equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

# KM Output
output_km = Entry(width=10, state="readonly")
output_km.grid(column=1, row=1)

# KM Label
km_label = Label(text="KM", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# Calculate Button
button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(column=1, row=3)

window.mainloop()
