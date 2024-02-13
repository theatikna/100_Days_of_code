from tkinter import *

def convert():
    try:
        value = float(entry.get())
        if unit_var.get() == "Miles to Kilometers":
            result = value * 1.60934
        elif unit_var.get() == "Kilometers to Miles":
            result = value / 1.60934
        result_label.config(text=f"{result:.2f} {result_unit[unit_var.get()]}")
    except ValueError:
        result_label.config(text="Invalid input")

window = Tk()
window.title("Unit Converter")
window.config(padx=20, pady=20)

unit_var = StringVar()
unit_var.set("Miles to Kilometers")
unit_options = ["Miles to Kilometers", "Kilometers to Miles"]
unit_menu = OptionMenu(window, unit_var, *unit_options)
unit_menu.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = Entry(width=10)
entry.grid(row=1, column=0, padx=5, pady=5)

convert_button = Button(text="Convert", command=convert)
convert_button.grid(row=1, column=1, padx=5, pady=5)

result_label = Label(text="", font=("Arial", 12, "bold"))
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_unit = {
    "Miles to Kilometers": "km",
    "Kilometers to Miles": "mi"
}

window.mainloop()
