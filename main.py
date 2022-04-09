# miles to kms convertor


from tkinter import *


def miles_to_km():
    miles = float(miles_entry.get())
    kms = round(miles * 1.60934, 2)
    km_result_label.config(text=f"{kms}")


window = Tk()
window.title("Mile to Km Convertor")
window.config(padx=30, pady=30)

miles_entry = Entry(width=7, font=("Arial", 14, 'normal'))
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 14, 'normal'))
miles_label.config(padx=5, pady=5)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 14, 'normal'))
is_equal_label.config(padx=5, pady=5)
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0", font=("Arial", 14, 'normal'))
km_result_label.config(padx=5, pady=5)
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 14, 'normal'))
km_label.config(padx=5, pady=5)
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km, font=("Arial", 14, 'normal'))
calculate_button.config(padx=5, pady=5)
calculate_button.grid(column=1, row=2)

window.mainloop()
